clc
clear
tdp = xlsread('Процессоры.xlsx', 'm2:m61')
potoki = xlsread('Процессоры.xlsx', 'g2:g61')
disp(' TDP           Потоки')
for i = 1:60
    fprintf(' %1i  ', tdp(i))
    fprintf(' %13i  \n', potoki(i))
end
sr_tdp = mean(tdp);
k_tdp = 0;
sr_potoki = mean(potoki);
k_potoki = 0;
for i = 1:60
    if tdp(i) > sr_tdp
        k_tdp = k_tdp + 1;
    end
    if potoki(i) > sr_potoki
        k_potoki = k_potoki + 1;
    end
end
k_tdp
k_potoki
temp = 0;
for i = 1:60
    for j = 1:59
        if potoki(j) < potoki(j + 1)
           temp = potoki(j);
           potoki(j) = potoki(j + 1);
           potoki(j + 1) = temp;
           temp = tdp(j);
           tdp(j) = tdp(j + 1);
           tdp(j + 1) = temp;
        end
    end
end
disp(' TDP           Потоки')
for i = 1:60
    fprintf(' %1i  ', tdp(i))
    fprintf(' %13i  \n', potoki(i))
end