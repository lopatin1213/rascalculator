from django.http import JsonResponse
from .models import ErrorLog

def send_errors(request):
    if request.method == 'POST':
        data = request.json()  # Получаем данные из тела запроса
        
        for item in data:
            # Проверяем наличие поля source, если оно отсутствует, ставим "Приложение"
            source_value = item.get('source', 'Приложение')
            
            # Создаем новую запись
            new_error = ErrorLog(
                error_type=item['error'],  # Тип ошибки
                version=item['version'],  # Версия приложения
                source=source_value  # Источник (либо email, либо "Приложение")
            )
            new_error.save()
        
        return JsonResponse({'message': 'Errors saved successfully'})
    else:
        return JsonResponse({'message': 'Invalid method'}, status=405)