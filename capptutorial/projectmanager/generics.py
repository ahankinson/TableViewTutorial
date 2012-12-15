from rest_framework import mixins
from rest_framework.generics import SingleObjectAPIView
from projectmanager.mixins import PartialUpdateModelMixin


class RetrievePartialUpdateDestroyAPIView(PartialUpdateModelMixin,
                                    mixins.RetrieveModelMixin,
                                    mixins.UpdateModelMixin,
                                    mixins.DestroyModelMixin,
                                    SingleObjectAPIView):
    @property
    def allowed_methods(self):
        """
        Return the list of allowed HTTP methods, uppercased.
        """
        self.http_method_names.append("patch")
        return [method.upper() for method in self.http_method_names
                if hasattr(self, method)]

    def get_serializer(self, instance=None, data=None, files=None, partial=False):
        """
        Return the serializer instance that should be used for validating and
        deserializing input, and for serializing output.
        """
        serializer_class = self.get_serializer_class()
        context = self.get_serializer_context()
        return serializer_class(instance, data=data, files=files, partial=partial, context=context)

    def patch(self, request, *args, **kwargs):
        return self.update_partial(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
