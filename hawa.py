# import complex math module
import cmath


print("helloo i am hawa")

name = "hawa adams"
has_eaten = True
numbers = 34






a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

# calculate the discriminant
d = (b ** 2) - (4 * a * c)

# find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)
print('The solution are {0} and {1}'.format(sol1, sol2))

# Python program to find roots of quadratic equation
import math


# function for finding roots
def findRoots(a, b, c):
    dis_form = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis_form))

    if dis_form > 0:
        print(" real and different roots ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif dis_form == 0:
        print(" real and same roots")
        print(-b / (2 * a))


    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)


a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))

# If a is 0, then incorrect equation
if a == 0:
    print("Input correct quadratic equation")

else:
    findRoots(a, b, c)
# #
# # import math
# # a = -1;
# # b = 1;
# # tol = 10^-3;
# # # iter = 0;
# # print('iter \t    a     \t       b      \t      fark\n' )
# # print('---------------------------------------------\n' )
# #
# #
# # import math
# # iter = 1
# # mData = []  #; % create an array
# # while (abs(a-b)>tol):
# #     fa = 2*math.sin(a) + 2*math.cos(a)
# #     fb = 2*math.sin(b) + 2*math.cos(b)
# #     m = (a+b)/2
# #     fm = 2*math.sin(m) + 2*math.cos(m)
# #     if (fa*fm<0):
# #         b=m
# #     else:
# #         a=m
# #
# #     mData[iter] = m#; % save data to array
# #     iter = iter + 1
# #     print('%d \t %f \f \t %f \t %f \t %f\n',iter,a,b, abs(a-b),tol)
# #
# #
# #
# # import matlab as plt
# # plt.plot(mData)#plot data
#
#
# # %% Asignment 2 is to solve an equation
# # x^2-3=0, for x in [1,2]
#
# # % Fill out the question marks to produce the appropriate results.
# # % Results : should be a plot as seen in the folder
#
# tol = 1.e-10     # % tolerance for errors
# a = 1.0
# b = 3.0  # % interval for the root
# nmax = 100 # % number of iterations
#
# #% Initialization
# itcount = 0
# error = 1.0
#
#
# def linspace(a, b):
#     return (a + b)/2
#
# #% Graph of the function
# xval = linspace(a, b)
#
#
# def fval(i):
#     pass
#
#
# def func():
#     pass
#
#
# for i in range(1, 100):
#     fval(i) = func(xval(i))
#
# #end
# plot(xval,fval);
# #grid on; hold on;
#
# #% iteration begins here
# while (itcount <= nmax && error >= tol):
#     itcount = itcount + 1;
#     % Generate and save iteratres
#     x = ???????? ##%% determine what goes here!!
#     z(itcount) = x
#     fa = func(a)
#     fb = func(b)
#     fx = func(x)
#     error = abs(fx)
#     if (error < tol)
#         x_final = x;
#     else
#         if (??????) % determine what goes here!
#             % root is between a and x
#             b = x;
#         else
#             % root is between x and b
#             a = x;
#         end
#     end
#     plot(z(1:itcount),zeros(itcount,1),'????')
#     pause(5)
# end
# if (itcount < nmax)
#     val = func(x);
#     fprintf(1,'Converged solution after %5d iterations',?????); % determine
#     fprintf(1,' is %15.7e, %e \n',??????, ?????); % determine
# else
#     fprintf(1,'Not converged after %5d iterations',nmax)
# end
#
# % this is the function value to solve
# function val = func(x)
# val = x^2 -3;
# end
#
