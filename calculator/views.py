from django.shortcuts import render

def calculate_view(request):
         
            context= { 
                    
            }
            if request.method == 'POST':
                form_data = request.POST
                print(form_data)
                number_a: str = form_data.get('number_a')
                number_b: str= form_data.get('number_b')
              #   operation = request.POST.get('operation')
                operation = form_data.keys()
              #   breakpoint()   tool used during debugging to pause your program at a specific line 
                print(f"Received {number_a},{number_b} and operationa{operation}")
                if number_a.isnumeric() and number_b.isnumeric():
                    #we do addition
                    number_a = float(number_a)
                    number_b = float(number_b)
                    if 'add' in operation:
                     total = number_a + number_b
                     context.update(
                            message = f"Addition total is {total}",
                     )
                    elif 'sub' in operation:
                     total = number_a - number_b
                     context.update(
                            message = f"Subtraction total is {total}",
                     )
                    elif 'mul' in operation:
                     total = number_a * number_b
                     context.update(
                            message = f"Multiplication total is {total}",
                     )
                    elif 'div' in operation:
                     total = number_a / number_b
                     context.update(
                            message = f"Division total is {total}",
                     )
                
                else:
                       context.update(
                              message = "Invalid input. Please enter numbers only.",
                              )


            return render(request,"calculator.html",context)
                


 


        