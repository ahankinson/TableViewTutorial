from django.http import Http404
from rest_framework import status
from rest_framework.response import Response


class PartialUpdateModelMixin(object):
    """
    Update a model instance.
    Should be mixed in with `SingleObjectBaseView`.
    """
    def update_partial(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            created = False
        except Http404:
            self.object = None
            created = True

        serializer = self.get_serializer(self.object, data=request.DATA, files=request.FILES, partial=True)

        if serializer.is_valid():
            self.pre_save(serializer.object)
            self.object = serializer.save()
            status_code = created and status.HTTP_201_CREATED or status.HTTP_200_OK
            return Response(serializer.data, status=status_code)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
