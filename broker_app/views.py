from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.core.paginator import Paginator
import datetime
from operator import *
from django.db.models.functions import ExtractMonth,ExtractYear,Coalesce
from django.db.models import Count,Sum,Q
from django.contrib import messages

# Create your views here.
def admin_login(request):
    error=""
    if request.method=='POST':
        name=request.POST['uname']
        pwd=request.POST['pwd']
        user=authenticate(username=name,password=pwd)
        try:

            if user.is_staff:
                login(request, user)
                return redirect('index')

                error = "no"
            else:
                # error = "yes"
                messages.error(request,'Invalid Credentials')
        except:
            messages.error(request,'Invalid Credentials')
            # error = "yes"

    return render(request,'login.html',{'error':error})
import calendar
def index(request):
    # debit_data=payments_tbl.objects.filter(description="Debit").annotate(month=ExtractMonth('date_added')).values('month').annotate(count=Count('id')).annotate(sum=Sum('amount')).values('month','sum','count').order_by('date_added__year')
    # credit_data=payments_tbl.objects.filter(description__startswith="profit").annotate(month=ExtractMonth('date_added')).values('month').annotate(sum=Sum('amount')).values('month','sum').order_by('date_added__year')
    # expense_data=payments_tbl.objects.all().annotate(month=ExtractMonth('date_added')).values('month').annotate(count=Count('id',filter=Q(description="Debit"))).annotate(sum=Sum('amount',filter=Q(description="Debit"))).values('month','count','sum').order_by('date_added__year','date_added__month')
    income_data=payments_tbl.objects.all().annotate(month=ExtractMonth('date_added')).values('month').annotate(count=Count('id',filter=Q(description__startswith="profit"))).annotate(sum=Sum('amount',filter=Q(description__startswith="profit"))).values('month','count','sum').order_by('date_added__year','date_added__month')
    expense_data=payments_tbl.objects.all().annotate(month=ExtractMonth('date_added')).values('month').annotate(count=Count('id',filter=Q(description="Debit"))).annotate(sum=Sum('amount',filter=Q(description="Debit"))).annotate(year=ExtractYear('date_added')).values('month','count','sum','year').order_by('date_added__year','date_added__month')
    year_list=[]
    month_list=[]
    debit_list=[]
    credit_list=[]
    for i in expense_data:
        month_list.append(calendar.month_name[i['month']])
        year_list.append(i['year'])


    for i in expense_data:
        if i['sum'] is None:
            debit_list.append(0.0)
        else:
            debit_list.append(i['sum'])

    # for i in expense_data:
    #     if i['sum'] is None:
    #         debit_list.append(0.0)
    #     else:
    #         debit_list.append(i['sum'])

    for i in income_data:
        if i['count']==0:
            credit_list.append(0.0)
        else:
            credit_list.append(i['sum'])
    
    print(month_list,debit_list,credit_list,year_list)
    context={
        'year_list':year_list,
        'month_list':month_list,
        'debit_list':debit_list,
        'credit_list':credit_list
    }
    return render(request,'index.html',context)

def add_investor(request):
    data=investors.objects.all()
    error=""
    if request.method=='POST':
        name=request.POST['name']
        try:
            if investors.objects.filter(name=name).exists():
                messages.error(request,name+' already taken')
                error="yes"
            else:
                obj=investors.objects.create(name=name)
                obj.save()
                messages.success(request,name+' successfully added')
        except:
            pass
    else:

        return render(request,'add_investor.html')
    return render(request,'add_investor.html',{'error':error,'data':data,'name':name})

def list_investors(request):
    obj=investors.objects.all()
    return render(request,'list_investors.html',{'data':obj})

def add_project(request):
    error=""
    if request.method=='POST':
        d=zip(
            request.POST.getlist('investor'),
            request.POST.getlist('share'),
        )
        data_dicts=[{
            'investor_name':investors.objects.get(name=investor),
            'share':share,
            'name':request.POST['name'],
        }
        for investor,share in d]
        print(data_dicts)
        for data in data_dicts:
            datas=projects.objects.create(**data)
            datas.save()
        messages.success(request,request.POST['name']+' added successfully')
    obj=investors.objects.all()
    return render(request,'add_project.html',{'data':obj,'error':error})

def list_projects(request):
    obj=projects.objects.all().distinct('name')
    return render(request,'list_projects.html',{'data':obj})


def view_project(request,name):
    data=projects.objects.filter(name=name)
    pr_name=name
    context={'data':data,'name':pr_name}
    return render(request,'project_view.html',context)

def add_profit(request):
    error=""
    project=projects.objects.all().distinct('name')
    if request.method=='POST':
        date=request.POST['date']
        project_name=request.POST['project']
        amount=request.POST['amount']
        number=float(amount)
        date_field=str(date)
        datas=profit_tbl.objects.create(projects=project_name,amount=amount,date_added=date_field)
        datas.save()
        filter_data=projects.objects.filter(name=project_name)
        for i in filter_data:
            investor_amount=number*(i.share/100)
            investor_name=i.investor_name.name
            print(investor_amount)
            obj=payments_tbl.objects.create(investor=investor_name,amount=investor_amount,date_added=date_field,description="profit for "+project_name)
            obj.save()
        messages.success(request,'Profit added successfully')
    return render(request,'add_profit.html',{'data':project,'error':error})
def view_profit(request):
    obj=profit_tbl.objects.all().order_by('date_added')
    paginator=Paginator(obj,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    nums="a" * page_obj.paginator.num_pages
    return render(request,'view_profit.html',{'data':obj,'num':nums,'page_obj':page_obj})

def view_payments(request):
    obj=payments_tbl.objects.all().order_by('date_added')
    paginator=Paginator(obj,5)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)
    nums="a" * page_obj.paginator.num_pages
    return render(request,'view_payments.html',{'data':obj,'num':nums,'page_obj':page_obj})

def add_payment(request):
    error=""
    obj=investors.objects.all()
    if request.method=='POST':
        investor=request.POST['investor']
        amount=request.POST['amount']
        amount_value=float(amount)
        print(type(amount_value))
        date=request.POST['date']
        date_field=str(date)
        payment=payments_tbl.objects.create(investor=investor,amount=amount_value,date_added=date_field,description="Debit")
        payment.save()
        messages.success(request,'Payment added successfully')
    return render(request,'add_payment.html',{'data':obj,'error':error})

def statements(request):
    error=""
    if request.method=='POST':
        a=request.POST['from_date']
        b=request.POST['to_date']
        invstr=request.POST['investor_name']
        start=str(a)
        end=str(b)
        if b < a:
            messages.error(request,'To date less than From date')
            error="yes"

        filtered_data=payments_tbl.objects.filter(date_added__range=(start,end),investor=invstr).order_by('date_added')
        # debit_filter=payments_tbl.objects.filter(description="Debit",date_added__range=(start,end),investor=invstr)
        debit_filter=payments_tbl.objects.filter(description="Debit",date_added__gte=start,date_added__lte=end,investor=invstr)     
        # credit_filter=payments_tbl.objects.filter(description__startswith="profit",date_added__range=(start,end),investor=invstr)
        credit_filter=payments_tbl.objects.filter(description__startswith="profit",date_added__gte=start,date_added__lte=end,investor=invstr)
        before_date_credit=payments_tbl.objects.filter(date_added__lt=start,investor=invstr,description__startswith="profit")
        before_date_debit=payments_tbl.objects.filter(date_added__lt=start,investor=invstr,description="Debit")
        total_debit=0
        for i in before_date_debit:
            res=total_debit+i.amount
            total_debit=res
        # print(total_debit)

        total_credit=0
        for i in before_date_credit:
            res=total_credit+i.amount
            total_credit=res
        # print(total_credit)

        debit=0
        for i in debit_filter:
            res=debit+i.amount
            debit=res
        # print(debit)

        credit=0
        for i in credit_filter:
            res=credit+i.amount
            credit=res
        # print(credit)

        opening_balance=total_credit - total_debit
        result=credit - debit
        balance=opening_balance + result

    else:
        data=investors.objects.all()
        return render(request,'demo_statement.html',{'data':data})
    data=investors.objects.all()
    return render(request,'demo_statement.html',{'data':data,'opening_balance':opening_balance,'result':balance,'new_data':filtered_data,'from':a,'to':b,'investor':invstr,'error':error})
