from django.shortcuts import render
def index (request):
    context = {
        'titulo':"Formulario",
    }
    
    return render(request, 'encuesta/volumen.html',context)

def enviar (request):
    context = {
        'titulo' : "Respuesta",
        'nombre' : request.POST['nombre'],
        'clave' : request.POST['password'],
        'educacion' : request.POST['educacion'],
        'nacionalidad' : request.POST['nacionalidad'],
        'idiomas' : request.POST.getlist('idiomas'),
        'correo' : request.POST['email'],
        'website' : request.POST['sitioweb'],
    }
    return render (request, 'encuesta/respuesta.html', context)


def resultados(request):
    numero1 = int(request.POST.get('numero1'))
    numero2 = int(request.POST.get('numero2'))
    operacion = request.POST.get('operacion', '')
    
    if operacion == 'suma':
        resultado = numero1 + numero2
    elif operacion == 'resta':
        resultado = numero1 - numero2
    elif operacion == 'multiplicacion':
        resultado = numero1 * numero2
    else:
        resultado = 0
    
    context = {
        'titulo': "Resultado de la operación",
        'operacion': operacion,
        'numero1': numero1,
        'numero2': numero2,
        'resultado': resultado,
    }
    return render(request, 'encuesta/resultado.html', context)

def volumenes(request):
    if request.method == 'POST':
        diametro = float(request.POST.get('diametro'))
        altura = float(request.POST.get('altura'))
        radio = diametro / 2
        volumen = 3.14159265359 * (radio ** 2) * altura
        return render(request, 'encuesta/resultadoV.html', {'volumen': volumen})
    
  





