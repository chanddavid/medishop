from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views
from .views import CompanyNameViewSet, MedicineNameViewSet

router = routers.DefaultRouter()
router.register("company", views.CompanyViewSet, basename="company")
router.register("companybank", views.CompanyBankViewSet, basename="companybank")
router.register("medicine", views.MedicineViewSet, basename="medicine")

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/gettoken/', TokenObtainPairView.as_view(), name="gettoken"),
    path('api/refresh_token/', TokenRefreshView.as_view(), name="refresh_token"),

    # namewish company search garna milxa
    path('api/companybyname/<str:name>/', CompanyNameViewSet.as_view(), name="companybyname"),
    path('api/medicinebyname/<str:name>/', MedicineNameViewSet.as_view(), name="medicinebyname"),

]
#{"name":"ibuprofen","medicine_type":"tablet","buying_price":"1000","selling_price":"2000","c_gst":"46","s_gst":"56",
#"batch_no":"5656","shelf_no":"4545","exp_date":"2020-01-23","mfg_date":"2020-09-29","company_id":"2",
#"description":"this this medicine of suyog's company","in_stock_total":"34","qty_in_strip":"34","medical_details":[{"salt_name":
# "salt1","salt_qty":"415","salt_qty_type":"mg","description":"this is salt1 details1"},{"salt_name":"salt2","salt_qty":"456","salt_qty_type":"mg","description":"this is salt2 details2"}]}