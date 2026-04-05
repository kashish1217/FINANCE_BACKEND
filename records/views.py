from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Record
from .serializers import RecordSerializer
from users.permissions import IsAdmin, IsAnalystOrAdmin

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.db.models import Sum
from django.db.models.functions import TruncMonth


# ✅ RECORD VIEWSET (THIS WAS MISSING)
class RecordViewSet(ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAdmin()]
        elif self.action in ['list', 'retrieve']:
            return [IsAnalystOrAdmin()]
        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def get_queryset(self):
        queryset = Record.objects.all()

        type_filter = self.request.query_params.get('type')
        category = self.request.query_params.get('category')

        if type_filter:
            queryset = queryset.filter(type=type_filter)
        if category:
            queryset = queryset.filter(category=category)

        return queryset


# ✅ SUMMARY API
@api_view(['GET'])
@permission_classes([IsAnalystOrAdmin])
def summary_view(request):

    total_income = Record.objects.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    total_expense = Record.objects.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0

    # Category breakdown
    categories = Record.objects.values('category').annotate(total=Sum('amount'))
    category_data = {item['category']: item['total'] for item in categories}

    # Recent transactions
    recent = Record.objects.order_by('-date')[:5].values()

    # 🔥 Monthly trends (NEW)
    monthly = (
        Record.objects
        .annotate(month=TruncMonth('date'))
        .values('month')
        .annotate(total=Sum('amount'))
        .order_by('month')
    )

    # 🔥 Improved response structure (NEW)
    return Response({
        "status": "success",
        "data": {
            "total_income": total_income,
            "total_expense": total_expense,
            "net_balance": total_income - total_expense,
            "category_breakdown": category_data,
            "recent_transactions": list(recent),
            "monthly_trends": list(monthly)
        }
    })