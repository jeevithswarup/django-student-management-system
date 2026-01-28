from rest_framework.response import Response # type: ignore
from rest_framework.views import APIView# type: ignore
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView # type: ignore
from rest_framework import viewsets # type: ignore
from rest_framework .decorators import api_view,permission_classes   # type: ignore
from rest_framework .permissions import AllowAny,IsAuthenticated,IsAdminUser # type: ignore
from rest_framework import status  # type: ignore
from api_work.models import Students
from  .serializers import StudentSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_portal(request):
    if request.method == 'GET':
        students=Students.objects.all()
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes([IsAdminUser])
def student_list(request):
    if request.method == 'GET':
        students=Students.objects.all() 
        serializer=StudentSerializer(students,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAdminUser])
def student_update(request,pk):
  try:
      student=Students.objects.get(pk=pk)
  except Students.DoesNotExist:
      return Response("{error:student doesn't exist}")
  if request.method == 'GET':
      serializer=StudentSerializer(student)
      return Response(serializer.data)
  elif request.method == 'PUT':
      serializer=StudentSerializer(student,data=request.data)
      if  serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
  elif request.method == 'DELETE':
      student.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
         
'''
class Student_list(APIView):

    def get(self,request):
        student=Students.objects.all()
        serializer=StudentSerializer(student,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class Student_update(APIView):
   def get_object(self,pk):
     try:
         return Students.objects.get(pk=pk)
     except Students.DoesNotExist:
         return None
 
   def get(self,request,pk):
        student=self.get_object(pk)  
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
   def put(self,request,pk):
       student=self.get_object(pk)
       if not student:
           return Response({"error":"Student not found"},status=status.HTTP_404_NOT_FOUND)
       serializer=StudentSerializer(student,data=request.data)
       if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

   def delete(self, request, pk):
        student = self.get_object(pk)
        if not student:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
'''
'''
class StudentListCreate(ListCreateAPIView):
    queryset=Students.objects.all()
    serializer_class=StudentSerializer
class StudentRetriveUpdateDelete(RetrieveUpdateDestroyAPIView):
    queryset=Students.objects.all()
    serializer_class=StudentSerializer    
'''
'''
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Students.objects.all()
    serializer_class=StudentSerializer    
'''