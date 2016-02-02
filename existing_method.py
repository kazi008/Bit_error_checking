import time
start_time = time.clock();

sentbyte1 = [1,1,1,0,1,1,1,0,1,0,0,0,1,1,1];
receivebyte1 = [1,1,0,0,1,1,1,0,1,0,0,0,1,0,1];

parity_information_bit1 = 0;
parity_check_bit1 = 0;
parity_information_bit2 = 0;
parity_check_bit2 = 0;


def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]

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

    return receivebyte1;



def parity_info_check(sentbyte1,receivebyte1):
        odd_even=0;
        even_odd=0;
        global parity_information_bit1,parity_check_bit1,parity_information_bit2,parity_check_bit2;
        for j in range(0,7):
            if receivebyte1[j] == 1:
                odd_even += 1;
            if sentbyte1[j] == 1:
                even_odd += 1;


        if odd_even%2 == 0:
            parity_information_bit2 = 0;
        else:
            parity_information_bit2 = 1;

        if even_odd%2 == 0:
            parity_information_bit1 = 0;
        else:
            parity_information_bit1 = 1;

        odd_even=0;
        even_odd=0;
        for j in range(7,15):
            if receivebyte1[j] == 1:
                odd_even += 1;
            if sentbyte1[j] == 1:
                even_odd += 1;

        if odd_even%2 == 0:
            parity_check_bit2 = 0;
        else:
            parity_check_bit2 = 1;

        if even_odd%2 == 0:
            parity_check_bit1 = 0;
        else:
            parity_check_bit1 = 1;


def information_bit_checking(receivebyte1):
    i=0;
    while True:
        b1 = receivebyte1[3]^receivebyte1[11]^receivebyte1[12]^receivebyte1[14];
        b2 = receivebyte1[1]^receivebyte1[5]^receivebyte1[13]^receivebyte1[14];
        b3 = receivebyte1[0]^receivebyte1[2]^receivebyte1[6]^receivebyte1[14];
        b4 = receivebyte1[7]^receivebyte1[8]^receivebyte1[10]^receivebyte1[14];

        print (receivebyte1,(b1+b2+b3+b4));
        if (b1+b2+b3+b4)>2:
            error_cycle = i;
            receivebyte1[14] ^= 1;
            #print("inverse 14th bit in cycle",i,"\n",receivebyte1);

        receivebyte1 = shift(receivebyte1,1);
        i += 1;
        if i==8:
            break
    receivebyte1 = shift(receivebyte1,7);
    #print ("error in",error_cycle,"number position");
    #print("corrected byte",receivebyte1);
    return receivebyte1;


def check_bit_checking(receivebyte1):
    i=0;
    while True:
        b1 = receivebyte1[3]^receivebyte1[11]^receivebyte1[12]^receivebyte1[14];
        b2 = receivebyte1[1]^receivebyte1[5]^receivebyte1[13]^receivebyte1[14];
        b3 = receivebyte1[0]^receivebyte1[2]^receivebyte1[6]^receivebyte1[14];
        b4 = receivebyte1[7]^receivebyte1[8]^receivebyte1[10]^receivebyte1[14];

        print (receivebyte1,(b1+b2+b3+b4));
        if (b1+b2+b3+b4)>2:
            error_cycle = i;
            receivebyte1[14] ^= 1;
            #print("inverse 14th bit in cycle",i,"\n",receivebyte1);

        receivebyte1 = shift(receivebyte1,-1);
        i += 1;
        if i==9:
            break
    receivebyte1 = shift(receivebyte1,9);
    #print ("error in",error_cycle,"number position");
    #print("corrected byte",receivebyte1);
    return receivebyte1;


def info_check_bit_checking(receivebyte1):
    check_bit_checking(receivebyte1);
    information_bit_checking(receivebyte1);

    return receivebyte1;



def error_correction(receivebyte1):
    if parity_information_bit1 != parity_information_bit2 and parity_check_bit1 == parity_check_bit2:
        print("error in information bit");
        return information_bit_checking(receivebyte1);
    elif parity_information_bit1 == parity_information_bit2 and parity_check_bit1 != parity_check_bit2:
        print("error in check bit");
        return  check_bit_checking(receivebyte1);
    elif parity_information_bit1 != parity_information_bit2 and parity_check_bit1 != parity_check_bit2:
        print("error in both information and check bit");
        info_check_bit_checking(receivebyte1);


    #print("after correction",receivebyte1);
    return sentbyte1,receivebyte1;



def error_check(sentbyte1,receivebyte1):

    global b1,b2,b3,b4,receive;
    i=0;
    receive = receivebyte1;
    while True:
        b1 = receivebyte1[3]^receivebyte1[11]^receivebyte1[12]^receivebyte1[14];
        b2 = receivebyte1[1]^receivebyte1[5]^receivebyte1[13]^receivebyte1[14];
        b3 = receivebyte1[0]^receivebyte1[2]^receivebyte1[6]^receivebyte1[14];
        b4 = receivebyte1[7]^receivebyte1[8]^receivebyte1[10]^receivebyte1[14];

        print (receivebyte1,(b1+b2+b3+b4));
        sh_i = i;
        if (b1+b2+b3+b4)>0:
            print("Errorneous byte");
            #shift(receivebyte1,-sh_i);
            print(receive);
            i=0;
            parity_info_check(sentbyte1,receive);
            receive = error_correction(receive);
            return receive;
            break

        receivebyte1 = shift(receivebyte1,-1);
        i += 1;
        if i==3:
            break
    receivebyte1 = shift(receivebyte1,i);
    return receive;


#parity_generate(sentbyte1,receivebyte1);
print(sentbyte1,"\n",receivebyte1);
receive = error_check(sentbyte1,receivebyte1);
receivebyte1 = receive;
print("receiveyte",receivebyte1);
#print (time.clock()-start_time);

