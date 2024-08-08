from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
from .models import item


# Create your views here.

# def find(req):
#     return render(req,'home.html',)

def find(req):
    page= loader.get_template('home.html')
    data={
        'val':'jack',
        'a':'hello',
    }

    response=page.render(data,req)
    return HttpResponse(response)



def homepage(req):
    page= loader.get_template('homepage.html')
    data={'category':'Applaincess',
          'product':[{
              'id:-':'001',
              'item':'washing machine',
              'brand':'LG',
              'spec':['5L','light weight','fully automatic']
              },{
              'id:-':'002',
              'item':'TV',
              'brand':'SONY',
              'spec':['8k FULL HD']
          },{
              'id:-':'003',
              'item':'fridg',
              'brand':'LG',
              'spec':['double door']
          },{
              'id:-':'004',
              'item':'AC',
              'brand':'samsung',
              'spec':['5Star']
          }
          ]}

    response=page.render(data,req)
    return HttpResponse(response)


def dbitemdisp(req):
    page= loader.get_template('dbitemdisp.html')
    db=item.objects.all()
    data={'pros':db}

    response=page.render(data,req)
    return HttpResponse(response)


def details(req,key):

    page= loader.get_template('productdetails.html')
    db=item.objects.get(id=key)

    data={'val':db}

    response=page.render(data,req)
    return HttpResponse(response)


# def addtocart(req):
    # print(req.GET['proid'])
    # print(req.GET['qty'])
    # responde=HttpResponse('item added to cart')
    # data=req.COOKIES.get('pid')
    # if data !=None:
    #     data=data+','+req.GET['proid']+':'+req.GET['qty']
    # else:
    #     data=req.GET['proid']+':'+req.GET['qty']

    # responde.set_cookie('pid',data)
    # return responde



# def shopingcart(req):
#     page= loader.get_template('shoppincart.html')
#     data=req.COOKIES.get('pid')
#     if data !=None:
#         item=data.split(',')
#         print(item)
#         value={}
#         for i in item:
#             cart=i.split(':')
#             print(cart)
#             proid=cart[0]
#             qty=cart[1]
#             value[proid]=qty
#         data={'mycart':value}
#         response=page.render(data,req)
#     else:
#         response=page.render({},req)
#     return HttpResponse(response)


def addtocart(req):
    proid=req.GET['proid']
    qty=req.GET['qty']
    print(proid)
    print(qty)
    cartitems={}
    response=HttpResponse('item add to cart')
    if req.session.__contains__('cartdata'):
        cartitems=req.session['cartdata']
    cartitems[proid]=qty
    req.session['cartdata']=cartitems
    print(cartitems)
    return response

  


def shopingcart(req):
    page= loader.get_template('shoppincart.html')
    if req.session.__contains__('cartdata'):
        print(req.session.keys())
        for key in req.session.keys():
            print(key)
            items=req.session[key].items()
            dbitems=[]
            for i in items:
                proid=i[0]
                qty=i[1]
                db=item.objects.get(id=proid)
                dbitems.append({
                    'id':proid,
                    'name':db.name,
                    'qty':qty,
                    'price':db.price,
                    't_price':int(qty)*db.price
                })
            fullamount=0
            for i in dbitems:
                for k,v in i.items():
                    if k =='t_price':
                        fullamount+=v

        data={'product':dbitems,'full':fullamount}
        response=page.render(data,req)
        return HttpResponse(response)
       
    else:
        return HttpResponse('no items added to cart')
  
    
def getalldata(req):
    data=[]
    for i in item.objects.all():
        data.append({
            'id':i.id,
            'name':i.name,
            'desc':i.desc,
            'price':i.price
        })
    newdata={'new':data}
    return JsonResponse(newdata)



def search(req):
    page= loader.get_template('productssearch.html')
    data={}
    response=page.render(data,req)
    return HttpResponse(response)


def getproduct(req,keyw):
    da=[]
    for i in item.objects.filter(name__contains=keyw):
        da.append({
            'id':i.id,
            'name':i.name,
            'desc':i.desc,
            'price':i.price
        })
    data={'produ':da} 
    return JsonResponse(data)
