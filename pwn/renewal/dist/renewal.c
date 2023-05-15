#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

char tmp[1];
int j;

#define readline_n(buf, n)          \
{                                   \
    for(j=0; j<n; j++)              \
    {                               \
        read(STDIN_FILENO, tmp, 1); \
        if (tmp[0] == '\n')         \
        {                           \
            break;                  \
        }                           \
        buf[j] = tmp[0];            \
    }                               \
}                                   \

struct Profile
{
    char name[0x10];
    char words[0x100];
    long age;
    char job[0x10];
};

void win()
{
    system("/bin/sh");
    return;
}

int main()
{
    struct Profile* p;
    setvbuf(stdout, (char*) NULL, _IONBF, 0);

    p = alloca(sizeof(struct Profile));
    memset(p, 0, sizeof(struct Profile));

    printf("Enter your profile\n");

    printf("Your Name > ");
    readline_n(p->name, sizeof(p->name));
    printf("Your Words > ");
    readline_n(p->words, sizeof(p->words));
    printf("Your Age > ");
    scanf("%ld", &p->age);
    printf("Desired Job > ");
    readline_n(p->job, sizeof(p->job));

    printf("\n---------------Profile---------------\n");
    printf("Name: \t\t%s\nWords: \t\t%s\nAge: \t\t%ld\nDesired Job: \t%s\n", p->name, p->words, p->age, p->job);
    printf("-------------------------------------\n\n");

    char check[4];
    int num, i=0;
    printf("Anything to fix?\n");
    do {
        printf("1. Name\n2. Words\n3. Age\n4. Desired Job\n> ");
        scanf("%d", &num);
        switch(num)
        {
            case 1:
                printf("Name > ");
                readline_n(p->name, sizeof(p->name));
                i++;
                break;
            case 2:
                printf("Words > ");
                readline_n(p->words, sizeof(p->words));
                i++;
                break;
            case 3:
                printf("Age > ");
                scanf("%ld", &p->age);
                i++;
                break;
            case 4:
                printf("Desired Job > ");
                readline_n(p->job, sizeof(p->words));
                i++;
                break;
            default:
                puts("Please specify 1, 2, 3 or 4");
                puts("Bye");
                exit(0);
        }
        if (i == 1)
        {
            printf("Done fixing?\n");
            readline_n(check, sizeof(check));
            if (strncmp(check, "YES", 3) == 0)
            {
                break;
            }
        }
    } while (i < 2);

    printf("Sent the profile.\n Good luck!\n");
    return 0;
}
