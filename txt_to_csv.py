import os
import csv

def create_chapters_csv_simple(folder_path, output_filename='corpus_chapters.csv'):
    """
    Создает CSV файл из текстовых файлов глав, находящихся в указанной папке.
    """
    
    with open(output_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Записываем заголовки
        writer.writerow(['chapter_number', 'chapter_name', 'text'])
        
        for i in range(1, 34):
            filename = f"{i}.txt"
            file_path = os.path.join(folder_path, filename)
            
            if not os.path.exists(file_path):
                continue
                
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    lines = file.readlines()
                
                if not lines:
                    continue
                
                chapter_name = lines[0].strip()
                
                if len(lines) >= 3:
                    text_lines = lines[2:]
                else:
                    text_lines = lines[1:] if len(lines) > 1 else []
                
                chapter_text = ''.join(text_lines).strip()
                
                # Записываем данные в CSV
                writer.writerow([i, chapter_name, chapter_text])
                print(f"Обработан файл: {filename}")
                
            except Exception as e:
                print(f"Ошибка при обработке файла {filename}: {e}")
    
    print(f"CSV файл создан: {output_filename}")

create_chapters_csv_simple("C:\\Users\\EPIX\\Documents\\laba_2\\The_Master_and_Margarita_rus") # Замените "[path]" на путь к вашей папке с текстовыми файлами
