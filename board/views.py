from django.shortcuts import render, get_object_or_404, redirect
from .models import Inquiry, CustomerMenu
from .forms import InquiryForm

# 목록
def inquiry_list(request):
    inquiries = Inquiry.objects.all().order_by('-created_at')
    return render(request, 'board/list.html', {'inquiries': inquiries})


# 상세
def inquiry_detail(request, pk):
    inquiry = get_object_or_404(Inquiry, pk=pk)
    return render(request, 'board/detail.html', {'inquiry': inquiry})


# 등록
def inquiry_create(request):
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inquiry_list')
    else:
        form = InquiryForm()

    return render(request, 'board/form.html', {'form': form})

def main_page(request):
    customer_menus = CustomerMenu.objects.prefetch_related('sub_menus').all()

    return render(
        request,
        'board/main.html',
        {
            'customer_menus': customer_menus
        }
    )