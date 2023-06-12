from django.urls import include, path
from tasks.urls import router
from tasks.views import get_tasks, make_payment

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('v1/api/get_tasks/', get_tasks),
    path('v1/api/make_payment/', make_payment),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
