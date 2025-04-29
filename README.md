##Міграція баз даних

Цей проєкт реалізовано в стилі Layered Architecture. Він дозволяє:

· Створювати структуру бази даних за допомогою ORM-моделей

· Зчитувати погодні дані з CSV-файлу

· Рефакторити та мігрувати структуру бази без втрати даних

· Створювати нові таблиці для впорядкування інформації

· Виводити погодні дані через консоль за запитом користувача

______________________________________________________________________________________

Технології

· Мова             Python

· БД               Postgres, MySQL

· Migration Tool   Flyway

· ORM              SQLAlchemy

· Клієнт БД       pgAdmin, MySQL Workbench

______________________________________________________________________________________

Структура проету на кожному етапі


• Stage1 

       - createDB.py                                                  	cтворення бази даних
       
       - connectDB	                                                        з’єданання до бази даних
       
       - models.py                                                          створення структуру бази даних за допомогою SQLAlchemy ORM моделі
       
       - migration.py                       	                        створення таблиць, які були описані в models.py
       
       - readData.py    	                                                заповнення таблиці даними, які були зчитані з GlobalWeatherRepository.csv 
       
       - main.py	                                                        організація і запуск всього процесу

       - GlobalWeatherRepository.csv                                        CSV-файл з погодними даними 


• Stage2

       - createDB.py                                                    
       
       - connectDB	                                                    
       
       - models.py                                                          додано клас для таблиці air_quality та змінено клас Weather
       
       - migration.py                       	                        додано функцію run_flyway_migrations, яка запускає міграції
       
       - readData.py    	                                               
         
       - main.py	                                                       
       
       - GlobalWeatherRepository.csv                                      

       - flyway.conf	                                                конфігурація в які містяться дані для підключення до бази та застосування міграцій 

       - sql                                                               директорія, в якій містяться SQL-скрипти для виконання
       
            V1___schema_history.sql  

            V2___create_air_quality.sql  	                створення таблиці 
                                                            air_quality

            V3___copy_data_from_weather_to_air_quality  	копіювання стовпців із 
                                                            таблиці weather до air_quality  
            
            V4___relation_table.sql                     	до таблиці weather додаємо рядок 
                                                            air_quality_id, який буде зовнішнім 
                                                            ключем

            V5___drop_columns_from_air_quality.sql          видалення із таблиці weather рядків, 
                                                            які були скопійовані до air_quality


• Stage3 

       - createDB.py                                                    
       
       - connectDB	                                                    
       
       - models.py                                                       
       
       - migration.py                       	                            
       
       - readData.py    	                                               
         
       - main.py	                                                       
       
       - GlobalWeatherRepository.csv                                      

       - flyway.conf	                                                   

       - sql                                                              
       
            V1___schema_history.sql  

            V2___create_air_quality.sql  	                

            V3___copy_data_from_weather_to_air_quality  	
            
            V4___relation_table.sql                     	

            V5___drop_columns_from_air_quality.sql        

            V6___add_column_to _air_quality.sql          створення стовпця going_outside, 
                                                         який заповнюється на основі формули


• Stage4

       - createDB.py                                                    
       
       - connectDB	                                                    
       
       - models.py                                                       
       
       - migration.py                       	                            
       
       - readData.py    	                                               
         
       - main.py	                                       додано функцію find_weather_info, яка
                                                           дає можливість користувачу задавши країну та дату, 
                                                           побачити всю інформацію стосовно погоди                                      
       
       - GlobalWeatherRepository.csv                                      

       - flyway.conf	                                                   

       - sql                                                              
       
            V1___schema_history.sql  

            V2___create_air_quality.sql  	                

            V3___copy_data_from_weather_to_air_quality  	
            
            V4___relation_table.sql                     	

            V5___drop_columns_from_air_quality.sql        

            V6___add_column_to _air_quality.sql          

 • Stage5

       - createDB.py                                                    
       
       - connectDB	                                                    
       
       - models.py                                                       
       
       - migration.py                       	                            
       
       - readData.py    	                                               
         
       - main.py	                                       додано функцію migrate_data, 
                                                           яка переносить дані з бази 
                                                           PostgreSQL у базу MySQL                                      
       
       - GlobalWeatherRepository.csv                                      

       - flyway.conf	                                                   

       - sql                                                              
       
            V1___schema_history.sql  

            V2___create_air_quality.sql  	                

            V3___copy_data_from_weather_to_air_quality  	
            
            V4___relation_table.sql                     	

            V5___drop_columns_from_air_quality.sql        

            V6___add_column_to _air_quality.sql     
