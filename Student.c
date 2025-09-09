#include <stdio.h>

// Define the structure
struct Student {
    char regNo[20];
    char surname[30];
    int yearOfStudy;
    char dob[15];
    float feesPaid;
};

int main() {
    struct Student s;

    // Input
    printf("Enter Registration Number: ");
    scanf("%s", s.regNo);

    printf("Enter Surname: ");
    scanf("%s", s.surname);

    printf("Enter Year of Study: ");
    scanf("%d", &s.yearOfStudy);

    printf("Enter Date of Birth (DD/MM/YYYY): ");
    scanf("%s", s.dob);

    printf("Enter Fees Paid for this Semester: ");
    scanf("%f", &s.feesPaid);

    // Output
    printf("\n--- Student Details ---\n");
    printf("Registration Number: %s\n", s.regNo);
    printf("Surname: %s\n", s.surname);
    printf("Year of Study: %d\n", s.yearOfStudy);
    printf("Date of Birth: %s\n", s.dob);
    printf("Fees Paid: %.2f\n", s.feesPaid);

    return 0;
}
