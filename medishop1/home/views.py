from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Company, CompanyBank, Medicine, MedicalDetails
from .serializers import CompanySerializer, CompanyBankSerializer, MedicineSerializer, MedicalDetailsSerializer


class CompanyViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        company = Company.objects.all()
        serializer = CompanySerializer(company, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Company List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CompanySerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Company Data Save Successfully"}
        except:
            dict_response = {"error": True, "message": "Error During Saving Company Data"}
        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializer(company, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Successfully Updated Company Data", "data": serializer.data}

        except:
            dict_response = {"error": True, "message": "Error During Updating Company Data"}
        return Response(dict_response)


class CompanyBankViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        companybank = CompanyBank.objects.all()
        serializer = CompanyBankSerializer(companybank, many=True, context={"request": request})
        response_dict = {"error": False, "message": "All Company Bank List Data", "data": serializer.data}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = CompanyBankSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Company Bank Data Save Successfully"}
        except:
            dict_response = {"error": True, "message": "Error During Saving Company Bank Data"}
        return Response(dict_response)
  #particular companybank lai id wish retrive garxa
    def retrieve(self, request, pk=None):
        queryset = CompanyBank.objects.all()
        companybank = get_object_or_404(queryset, pk=pk)
        serializer = CompanyBankSerializer(companybank, context={"request": request})
        return Response({"error": False, "message": "Single Data Fetch", "data": serializer.data})

    def update(self, request, pk=None):
        try:
            queryset = CompanyBank.objects.all()
            companybank = get_object_or_404(queryset, pk=pk)
            serializer = CompanyBankSerializer(companybank, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Successfully Updated Companybank Data",
                             "data": serializer.data}

        except:
            dict_response = {"error": True, "message": "Error During Updating Companybank Data"}
        return Response(dict_response)

#namewish bank search garna milxa
class CompanyNameViewSet(generics.ListAPIView):
    serializer_class = CompanySerializer
    def get_queryset(self):
        name=self.kwargs["name"]
        return Company.objects.filter(name=name)



class MedicineViewSet(viewsets.ViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        medicine = Medicine.objects.all()
        serializer = MedicineSerializer(medicine, many=True, context={"request": request})
        #for medicine details data
        medicine_data=serializer.data
        newmedicinelist=[]

        #adding extra key for medicine details in Medicine
        for medicine in medicine_data:
            #accessing all the medicine details of current Medicine id
            medicine_details=MedicalDetails.objects.filter(medicine_id=medicine["id"])
            medicine_details_serializers=MedicalDetailsSerializer(medicine_details,many=True)
            medicine["medicine_details"]=medicine_details_serializers.data
            newmedicinelist.append(medicine)

        response_dict = {"error": False, "message": "All Medicine List Data", "data": newmedicinelist}
        return Response(response_dict)

    def create(self, request):
        try:
            serializer = MedicineSerializer(data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            #for multiple serializer in same view set
            medicine_id=serializer.data['id'];

            #access the serializer id which just save in our database table
            #print(medicine_id)
            #adding and saving id into medicine details table
            medicine_details_list=[]
            for medicine_details in request.data["medicine_details"]:
                print(medicine_details)
                #adding medicine id which will work for medical details serializer
                medicine_details['medicine_id']=medicine_id
                medicine_details_list.append(medicine_details)
                print(medicine_details)
            serializer2= MedicalDetailsSerializer(data=medicine_details_list,many=True,context={"request":request})
            serializer2.is_valid()
            serializer2.save()





            dict_response = {"error": False, "message": "Medicne Data Save Successfully"}
        except:
            dict_response = {"error": True, "message": "Error During Saving Medicine Data"}
        return Response(dict_response)

    def update(self, request, pk=None):
        try:
            queryset = Medicine.objects.all()
            medicine = get_object_or_404(queryset, pk=pk)
            serializer = CompanySerializer(medicine, data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dict_response = {"error": False, "message": "Successfully Updated Medicine Data", "data": serializer.data}

        except:
            dict_response = {"error": True, "message": "Error During Updating Medicine Data"}
        return Response(dict_response)

class MedicineNameViewSet(generics.ListAPIView):
    serializer_class = MedicineSerializer
    def get_queryset(self):
        name=self.kwargs["name"]
        return Medicine.objects.filter(name=name)




company_list = CompanyViewSet.as_view({"get": "list"})
company_create = CompanyViewSet.as_view({"post": "create"})
company_update = CompanyViewSet.as_view({"put": "update"})
