import csv
chosen_subjects = {}
chosen_slots =[]
data={}
def priority(s)->int:
    lp=[]
    if "+" not in s:
        ls=[s]
    else:
        ls=s.split("+")
    for i in ls:
        count = 0
        for j in i:
            count += ord(j)
        lp.append(count)
    count = min(lp)
    return count

def read_data(file_path):
    global data
    sub=data
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        data1 = list(reader)
    for row in data1:
        if row[1] not in sub:
            sub[row[1]] = [row[1:]]
        else:
            sub[row[1]].append(row[1:])
        
    for key in sub:
        sub[key].sort(key=lambda x: priority(x[-1]), reverse=True)
def find_latest_slot(sub_code):
    global data, chosen_slots
    latest_slot = None
    for subject in data:
        if subject == sub_code:
            for slot in data[subject]:
                if slot[-1] not in chosen_slots:
                    latest_slot = slot[-1]
                    break
            break
    return latest_slot

def select_subject():
    global chosen_subjects , data
    while True:
        subject = input("Enter a subject to choose (or 'q' to quit): ").strip().upper()
        if subject == 'Q':
            break
        if subject not in data:
            print("Invalid subject! Please choose a valid subject.")
            continue
        slot = find_latest_slot(subject)
        if not slot:
            print("Slot clashing! Please choose a different subject.")
            continue
        if subject in chosen_subjects:
            print("Subject already chosen! Please choose a different subject.")
            continue
        chosen_subjects.update({subject:slot})
        chosen_slots.append(slot)
        print(f"Latest slot chosen for {subject}: {slot}")

def display_subjects(data):
    for subject in data:
        slots = [slot[-1] for slot in data[subject]]
        print(f"{subject}: {' , '.join(slots)}")

def display_chosen_subjects(chosen_subjects):
    for subject, slot in chosen_subjects.items():
        print(f"Chosen subject: {subject}, Slot: {slot}")

def delete_subject(chosen_subjects, chosen_slots, subject):
    if subject in chosen_subjects:
        slot = chosen_subjects[subject]
        del chosen_subjects[subject]
        chosen_slots.remove(slot)
        print(f"Deleted subject: {subject}")
    else:
        print("Subject not found in chosen subjects.")


read_data('data.csv')

print("Welcome to the Mock FFCS!")
while True:
    print("\nMenu:")
    print("1. Display available subjects")
    print("2. Select a subject")
    print("3. Delete a subject")
    print("4. Show selected subjects")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ").strip()
    if choice == '1':
        display_subjects(data)
    elif choice == '2':
        select_subject()
    elif choice == '3':
        subject = input("Enter the subject to delete: ").strip().upper()
        delete_subject(chosen_subjects, chosen_slots, subject)
    elif choice == '4':
        display_chosen_subjects(chosen_subjects)
    elif choice == '5':
        print("Thank you for using the Mock FFCS\n A Program TBA5854!")
        break
    else:
        print("Invalid choice! Please choose a valid option.")