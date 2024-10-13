# Question 1 for Python Project: Course PROG 101 @ Saras AI Institute
# Submitted by Group 5 (Gaurav R Malik and Lakshya Manchanda)

# Defining the default filename and option.
file_name = 'Nil'
option = '0'

# Defining the while loop to keep the application running
while(option != '5'):

    print('')
    print('Developer Menu')
    print('===============================================================================')
    print('')
    print('1. Load Song Data')
    print('2. View Songs Database')
    print('3. Delete a Song')
    print('4. Modify a Song')
    print('5. Exit')
    print('')
    print('Select an Option:',end = "")
    option = input()
    print('')
    print('')

    # Deliverable for Option 1: Load Song Data
    if option == '1':
        print('Enter the file name to load songs',end = "")
        print('')
        file_name = input()

        # Exception handling for file name, in case the file does not exist.
        try:
            file = open(file_name,'r')
            print(f'Songs loaded from {file_name}')
            file.close()
        except:
            print('This filename does not exist in our record... Please check again at your end.')
            print('Going back to the home page')
            print('')

    
    # Deliverable for Option 2: View Songs Database
    if option == '2':

        if file_name == 'Nil':
            print('No file specified. Please specify the file.')
            print('Defaulting to home screen')
            print('')

        else:
            title = []
            artist = []
            genre = []
            file = open(file_name,'r')
            lines = file.readlines()

            for line in lines:
                data = line.split(',')
                title.append(data[0])
                artist.append(data[1])
                genre.append(data[3])
            file.close()

            len_max_1 = max(len('Title'),max([len(item) for item in title]))
            len_max_2 = max(len('Artist'),max([len(item) for item in artist]))
            len_max_3 = max(len('Genre'),max([len(item) for item in genre]))

            print('Song Database')
            print('Title'.ljust(len_max_1+5),'Artist'.ljust(len_max_2+5),'Genre'.ljust(len_max_3+5))
            print('')
            for i in range(0,len_max_1 + len_max_2 + len_max_3 + 15):
                print('=',end = "")
            
            print('')

            for i in range(0,len(title)):
                print(title[i].ljust(len_max_1+5),artist[i].ljust(len_max_2+5),genre[i].ljust(len_max_3+5))
    
    
    # Deliverable for Option 3: Delete a Song
    if option == '3':

        if file_name == 'Nil':
            print('No file specified. Please specify the file.')
            print('Defaulting to home screen')
            print('')

        else:
            print('Enter artist name for song to be deleted: ',end = "")
            singer = input()
            print('')
            print('Enter title for song to be deleted: ',end = "")
            song_name = input()
            print('')

            file = open(file_name,'r')
            lines = file.readlines()
            
            total_lines = 0
            for line in lines:
                total_lines += 1 
            
            line_number = 0
            for line in lines:
                data = line.split(',')
                if song_name.lower() in data[0].lower() and singer.lower() in data[1].lower():
                    break
                line_number += 1

            file.close()

            if (line_number == total_lines):
                print('The required song is not found')
                print('Going to home page')
                print('')
            
            else:
                file = open(file_name,'w')
                curr_line = -1
                for line in lines:
                    curr_line += 1
                    if curr_line != line_number:
                        file.write(line)
                
                file.close()
                print(f'Deleted song {song_name} by {singer}')

    
    # Deliverable for Option 4: Modify a Song
    if option == '4':

        if file_name == 'Nil':
            print('No file specified. Please specify the file.')
            print('Defaulting to home screen')
            print('')

        else:
            print('Enter artist name for song to be modified:',end = "")
            singer = input()
            print('')

            print('Enter title for song to be modified:',end = "")
            song_name = input()
            print('')

            file = open(file_name,'r')
            lines = file.readlines()
            
            total_lines = 0
            for line in lines:
                total_lines += 1 
            
            line_number = 0
            for line in lines:
                data = line.split(',')
                if song_name.lower() in data[0].lower() and singer.lower() in data[1].lower():
                    print('Current Details:')
                    print('Album',data[2],', Genre',data[3],', Duration',data[4])
                    break
                line_number += 1

            file.close()

            if (line_number == total_lines):
                print('The required song is not found')
                print('Going to home page')
                print('')

            else:
                print('Enter new album (or Press Enter to keep current):',end = "")
                album = input()
                print('Enter new genre (or Press Enter to keep current):',end = "")
                genre = input()
                print('Enter new duration (or Press Enter to keep current):',end = "")
                duration = input()
                print('')

                if album != '':
                    data[2] = '\"' + album + '\"'

                if genre != '':
                    data[3] = '\"' + genre + '\"'

                if duration != '':
                    data[4] = '\"' + duration + '\"'
                
                file = open(file_name,'w')
                curr_line = -1
                for line in lines:
                    curr_line += 1
                    if curr_line != line_number:
                        file.write(line)

                    else:
                        file.write(','.join(data))

                file.close()
                print(f'Modified song {song_name} by {singer}')


# Condition for Option 5: Exit the Application
if option == '5':
    print('Exiting Application. Goodbye!')
    print('')