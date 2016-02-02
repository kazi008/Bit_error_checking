import time

from collections import OrderedDict

sender_dict = OrderedDict((k, v) for k,v in [["sentbyte1" , [1,1,1,0,1,1,1]],
    ["sentbyte2" , [0,0,1,0,0,1,0]],
    ["sentbyte3" , [1,0,0,1,0,1,1]],
    ["sentbyte4" , [1,1,1,0,0,1,0]]])

a_dict=OrderedDict((k, v) for k,v in [["a",1],["b",2],["c",3]])
receiver_dict = OrderedDict((k, v) for k,v in [["receivebyte1" , [1,1,1,0,0,1,1]],
    ["receivebyte2" , [0,0,1,0,0,1,0]],
    ["receivebyte3" , [1,0,0,1,0,1,1]],
    ["receivebyte4" , [1,1,1,0,0,1,0]]])

start_time = time.clock();


def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]

def majority_checking(receivebyte1):

    global b1,b2,b3,b4;
    i=0;
    while True:
        if (receivebyte1[3]+receivebyte1[11]+receivebyte1[12]+receivebyte1[14])%2 != 0:
            b1 = 1;
        else:
            b1 = 0;
        if (receivebyte1[1]+receivebyte1[5]+receivebyte1[13]+receivebyte1[14])%2 != 0:
            b2 = 1;
        else:
            b2 = 0;
        if (receivebyte1[0]+receivebyte1[2]+receivebyte1[6]+receivebyte1[14])%2 != 0:
            b3 = 1;
        else:
            b3 = 0;
        if (receivebyte1[7]+receivebyte1[8]+receivebyte1[10]+receivebyte1[14])%2 != 0:
            b4 = 1;
        else:
            b4 = 0;

        print (receivebyte1,(b1+b2+b3+b4));
        if (b1+b2+b3+b4)>2:
            error_cycle = i;
            if receivebyte1[14] == 0:
                receivebyte1[14] = 1;
                print("inverse 14th bit in cycle",i,"\n",receivebyte1);
            else:
                receivebyte1[14] = 0;
                print("inverse 14th bit in cycle",i,"\n",receivebyte1);

        receivebyte1 = shift(receivebyte1,1);
        i += 1;
        if i==8:
            break
    receivebyte1 = shift(receivebyte1,7);
    print ("error in",error_cycle,"number position");
    return receivebyte1;

    print(time.time());


def parity_generate(sentbyte1,receivebyte1):
    if (sentbyte1[0]+sentbyte1[1]+sentbyte1[3])%2 != 0:
        receivebyte1.append(1);
    else:
        receivebyte1.append(0);
    if (sentbyte1[1]+sentbyte1[2]+sentbyte1[4])%2 != 0:
        receivebyte1.append(1);
    else:
        receivebyte1.append(0);
    if (sentbyte1[2]+sentbyte1[3]+sentbyte1[5])%2 != 0:
        receivebyte1.append(1);
    else:
        receivebyte1.append(0);
    if (sentbyte1[3]+sentbyte1[4]+sentbyte1[6])%2 != 0:
        receivebyte1.append(1);
    else:
        receivebyte1.append(0);
    if (sentbyte1[0]+sentbyte1[1]+sentbyte1[3]+sentbyte1[4]+sentbyte1[5])%2 != 0:
        receivebyte1.append(1);
    else:
        receivebyte1.append(0);
    if (sentbyte1[1]+sentbyte1[2]+sentbyte1[4]+sentbyte1[5]+sentbyte1[6])%2 != 0:
        receivebyte1.append(1);
    else:
        receivebyte1.append(0);
    if (sentbyte1[0]+sentbyte1[1]+sentbyte1[2]+sentbyte1[5]+sentbyte1[6])%2 != 0:
        receivebyte1.append(1);
    else:
        receivebyte1.append(0);
    if (sentbyte1[0]+sentbyte1[2]+sentbyte1[6])%2 != 0:
        receivebyte1.append(1);
    else:
        receivebyte1.append(0);

    receive = majority_checking(receivebyte1);
    return receive;
    print(time.time());

def parity_of_byte_sender():
    for key, value in sender_dict.items():
        odd_even=0;
        temp = value;
        for j in range(0,7):
            if temp[j] == 1:
                odd_even += 1;

        if odd_even%2 == 0:
            temp.append(0);
            value = temp;
        else:
            temp.append(1);
            value = temp;


def parity_of_byte_receiver():
    for key, value in receiver_dict.items():
        odd_even=0;
        temp = value;
        for j in range(0,7):
            if temp[j] == 1:
                odd_even += 1;

        if odd_even%2 == 0:
            temp.append(0);
            value = temp;
        else:
            temp.append(1);
            value = temp;


parity_of_byte_sender();
parity_of_byte_receiver();
error_exist = counter = 0;

for (k,v),(k1,v1) in zip(sorted(sender_dict.items()),sorted(receiver_dict.items())):
    temp1 = v;
    temp2 = v1;
    if temp1[7] != temp2[7]:
        temp1 = temp1[:-1];
        temp2 = temp2[:-1];
        v = temp1;
        v1 = temp2;
        print("error in",counter+1,"number byte");
        #print(temp1,temp2);
        tem = parity_generate(temp1,temp2);
        v1 = tem;
        v1 = v1[:-8];
        #print("this is ",v1);
        error_exist = 1;
    counter += 1;
if error_exist != 1:
    print("No Error");

print("corrected receivebytes",receiver_dict['receivebyte1'],receiver_dict['receivebyte2'],receiver_dict['receivebyte3'],receiver_dict['receivebyte4']);
#print(start_time);
print (time.clock()-start_time);

