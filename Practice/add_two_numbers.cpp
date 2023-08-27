#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        
        ListNode* curr = nullptr;
        ListNode* prev = nullptr;
        ListNode* result = nullptr;

        ListNode* n1 = l1;
        ListNode* n2 = l2;

        int ones = 0;
        int carry = 0;
        int sum = 0;

        while ( !(n1 == nullptr || n2 == nullptr))
        {
            if (n1 != nullptr && n2 != nullptr)
            {
                int k1 = n1->val;
                int k2 = n2->val;

                sum = k1 + k2 + carry;
                ones = sum % 10;
                carry = sum / 10;

                curr = new ListNode(ones);
                if (prev == nullptr)
                    prev = curr;
                else
                    prev->next = curr;

                n1 = n1->next;
                n2 = n2->next;

                printf("%d", ones);

            }
            else if(n1 == nullptr && n2 != nullptr)
            {
                sum = n2->val + carry;
                ones = sum % 10;
                carry = sum / 10;

                curr = new ListNode(ones);
                if (prev == nullptr)
                    prev = curr;
                else
                    prev->next = curr;

                n1 = n1->next;
                n2 = n2->next;
            }
            else if(n2 == nullptr && n1 != nullptr)
            {
                sum = n1->val + carry;
                ones = sum % 10;
                carry = sum / 10;

                curr = new ListNode(ones);
                if (prev == nullptr)
                    prev = curr;
                else
                    prev->next = curr;

                n1 = n1->next;
                n2 = n2->next;
            }
            else if(n1 == nullptr && n2 == nullptr)
            {
                break;
            }

            if (result == nullptr && curr != nullptr)
            {
                result = curr;
            }
        }

        return result;
    }
};

void printNum(std::string name, ListNode* num)
{
    ListNode* digit = num;
    cout << name << ": ";
    while(digit != nullptr)
    {
        printf("%d", digit->val);
        digit = digit->next;
    }
    printf("\n");
}

int main()
{
    ListNode* l1 = new ListNode(2);
    ListNode* l2 = new ListNode(4);
    ListNode* l3 = new ListNode(3);

    ListNode* l4 = new ListNode(5);
    ListNode* l5 = new ListNode(6);
    ListNode* l6 = new ListNode(4);

    l1->next = l2;
    l2->next = l3;

    l4->next = l5;
    l5->next = l6;

    printNum("N1", l1);
    printNum("N2", l4);

    Solution s;
    ListNode* result = s.addTwoNumbers(l1, l4);

    printNum("Result", result);

    return 0;
}