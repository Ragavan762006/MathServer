from django.shortcuts import render
def rectarea(request):
    context={}
    context['area'] = "0"
    context['b'] = "0"
    context['h'] = "0"
    if request.method == 'POST':
        print("POST method is used")
        b = request.POST.get('length','0')
        h = request.POST.get('height','0')
        print('request=',request)
        print('length=',b)
        print('height=',h)
        area = 2*(int(b) * int(b))+4*int(b)*int(h)
        context['area'] = area
        context['b'] = b
        context['h'] = h
        print('Area=',area)
    return render(request,'mathapp/math.html',context)
