clear
clc
% tugas nomor 2

d = 20;
%N = 6;
k = linspace(0,0.2,10000);

for i = 1:12
    ihf(d,i)
    hold on;
    axis([00 0.2 -45 20]);
    grid on;
end

function ihf(d, N)
    k = linspace(0,0.2,10000);
    a = N*sin(pi*d*N*k);
    b = N*sin(pi*d*k);
    
    dB=20*log10(a./b);

    plot(k,dB)
end
