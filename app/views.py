from django.shortcuts import render
from .tasks import add, mul, xsum


def sum_without_celery(a, b):
    return a + b

def test_view(request):
    
    result_add = add.delay(4000000, 6000000)
    result_mul = mul.delay(4, 6)
    result_xsum = xsum.delay([1, 2, 3, 4, 5])
    result_without_celery = sum_without_celery(4, 6)
    
    
    try:
        result_add = result_add.get(timeout=5)
        result_mul = result_mul.get(timeout=5)
        result_xsum = result_xsum.get(timeout=5)

        context = {
            'add_result': result_add,
            'mul_result': result_mul,
            'xsum_result': result_xsum,
            'without_celery_result': result_without_celery,
        }
        
    except Exception as e:
        print(f"Error retrieving task results: {e}")
        context = {}
        context.update({
            'add_result': 'Could not retrieve result in time',
            'mul_result': 'Could not retrieve result in time',
            'xsum_result': 'Could not retrieve result in time',
            'without_celery_result': result_without_celery,
        })

    return render(request, 'test_view.html', context)

