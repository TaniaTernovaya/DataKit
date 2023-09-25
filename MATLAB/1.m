% нахожу общее решение диф уравнения
syms x y(x);
eqn = x^2 * diff(y, x) + y == 0;
sol = dsolve(eqn);
disp('Общее решение:');
disp(sol);

% нахожу общее решение диф уравнения
general_solution = dsolve(eqn);
x_value = 1;
particular_solution = subs(general_solution, x, x_value);
disp('Частное решение:');
disp(particular_solution);

syms x;
general_solution = dsolve(x^2 * diff(y, x) + y == 0);
x_value = 1;
particular_solution = subs(general_solution, x, x_value);
x_interval = [1, 10]; 
f = matlabFunction(particular_solution);

% Строю график частного решения
fplot(f, x_interval, 'b--', 'LineWidth', 3);
xlabel('x');
ylabel('y');
title('Частное решение: y(x) = e^{1/x}');
grid on;