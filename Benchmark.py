import math
import sys

import numpy as np

"""
The Benchmarks for boundary identification
    input:
        fun_name__: str format. The name of the called benchmark
        performance_mode_num: int format. 2 or 4. The number of decision modes
        input_points: the coordinates of the input points
    output:
        result: the decision modes corresponding to the input points
    example:
        benchmark = Benchmark("Benchmark1",2)
        x=[1,2]
        y = benchmark.run(x)
"""

class Benchmark:
    def __init__(self, fun_name__, performance_mode_num__=2):
        self.performance_mode_num = performance_mode_num__  # the number of decision modes
        self.function_name = ["Benchmark1", "Benchmark2", "Benchmark3", "Benchmark4", "Benchmark5",
                              "Benchmark6", "Benchmark7", "Benchmark8", "Benchmark9"]
        self.name = fun_name__
        self.fun_num = self.function_name.index(self.name)+1  # index of the Benchmark
        # 问题范围
        if self.fun_num == 1:
            self.problem_range = 4
            self.run_time = 4.8828125e-06
            self.initial_points_num = 50
        elif self.fun_num == 2:
            self.problem_range = 10
            self.run_time = 4.8828125e-06
            self.initial_points_num = 80
        elif self.fun_num == 3:
            self.problem_range = 50
            self.run_time = 2.44140625e-06
            self.initial_points_num = 150
        elif self.fun_num == 4:
            self.problem_range = 500
            self.run_time = 4.8828125e-06
            self.initial_points_num = 300
        elif self.fun_num == 5:
            self.problem_range = 10
            self.run_time = 4.8828125e-06
            self.initial_points_num = 80
        elif self.fun_num == 6:
            self.problem_range = 50
            self.run_time = 2.44140625e-06
            self.initial_points_num = 150
        elif self.fun_num == 7:
            self.problem_range = 10
            self.run_time = 7.32421875e-06
            self.initial_points_num = 80
        elif self.fun_num == 8:
            self.problem_range = 20
            self.run_time = 2.44140625e-06
            self.initial_points_num = 100
        elif self.fun_num == 9:
            self.problem_range = 4
            self.run_time = 4.8828125e-06
            self.initial_points_num = 50

    def run(self, input_point):
        if self.fun_num == 1:
            result = self.benchmark1(input_point)
        elif self.fun_num == 2:
            result = self.benchmark2(input_point)
        elif self.fun_num == 3:
            result = self.benchmark3(input_point)
        elif self.fun_num == 4:
            result = self.benchmark4(input_point)
        elif self.fun_num == 5:
            result = self.benchmark5(input_point)
        elif self.fun_num == 6:
            result = self.benchmark6(input_point)
        elif self.fun_num == 7:
            result = self.benchmark7(input_point)
        elif self.fun_num == 8:
            result = self.benchmark8(input_point)
        elif self.fun_num == 9:
            result = self.benchmark9(input_point)
        return result

    # 2-d
    def benchmark1(self, input_point):
        dim = len(input_point)
        if dim == 2:
            x = input_point[0]
            y = input_point[1]
            temp1 = math.exp(-math.pow(x, 2) - math.pow(y+1, 2))
            temp2 = math.exp(-math.pow(x, 2) - math.pow(y, 2))
            temp3 = math.exp(-math.pow(x+1, 2) - math.pow(y, 2))
            try:
                result = 5*math.pow(1-x, 2)*temp1 - 5*(x/5-math.pow(y, 5))*temp2 - 6*temp3
            except Exception as e:
                print('error:wrong range')
                print(e)
                sys.exit()
            # 根据性能模式个数进行判断
            if self.performance_mode_num == 2:
                threshold_value = 0
                if result < threshold_value:
                    result = 0
                else:
                    result = 1
            elif self.performance_mode_num == 3:
                threshold_value1 = 0
            elif self.performance_mode_num == 4:
                threshold_value1 = -2
                threshold_value2 = 0
                threshold_value3 = 2
                if result < threshold_value1:
                    result = 0
                elif threshold_value1 <= result < threshold_value2:
                    result = 1
                elif threshold_value2 <= result < threshold_value3:
                    result = 2
                elif result >= threshold_value3:
                    result = 3
        else:
            result = -1
            print('**************The dimension is not supported***************')
        return result

    # any dimension
    def benchmark2(self, input_point):
        dim = len(input_point)
        temp1 = 0
        temp2 = 1
        for i in range(0, dim):
            temp1 = temp1 + math.pow(input_point[i], 2)/4000
            temp2 = temp2 * math.cos(input_point[i]/math.pow(i+1, 0.5))
        result = temp1 - temp2 + 1
        if self.performance_mode_num == 2:
            threshold_value = 1
            if result < threshold_value:
                result = 0
            else:
                result = 1
        elif self.performance_mode_num == 3:
            threshold_value1 = 0
        elif self.performance_mode_num == 4:
            threshold_value1 = 0.6
            threshold_value2 = 1.2
            threshold_value3 = 1.8
            if result < threshold_value1:
                result = 0
            elif threshold_value1 <= result < threshold_value2:
                result = 1
            elif threshold_value2 <= result < threshold_value3:
                result = 2
            elif result >= threshold_value3:
                result = 3
        return result

    # any dimension
    def benchmark3(self, input_point):
        dim = len(input_point)
        para_a = 20
        para_b = 0.2
        para_c = 2*math.pi
        temp1 = 0
        temp2 = 0
        for i in range(0, dim):
            temp1 = temp1 + math.pow(input_point[i], 2)
            temp2 = temp2 + math.cos(para_c*input_point[i])

        result = -para_a*math.exp(-para_b*math.pow(1/dim*temp1, 0.5)) - math.exp(1/dim*temp2) + para_a + math.exp(1)
        if self.performance_mode_num == 2:
            threshold_value = 17
            if result < threshold_value:
                result = 0
            else:
                result = 1
        elif self.performance_mode_num == 3:
            threshold_value1 = 0
        elif self.performance_mode_num == 4:
            threshold_value1 = 10
            threshold_value2 = 11
            threshold_value3 = 12
            if result < threshold_value1:
                result = 0
            elif threshold_value1 <= result < threshold_value2:
                result = 1
            elif threshold_value2 <= result < threshold_value3:
                result = 2
            elif result >= threshold_value3:
                result = 3
        return result

    # any dimension
    def benchmark4(self, input_point):
        dim = len(input_point)
        temp1 = 0
        for i in range(0, dim):
            temp1 = temp1 + input_point[i]*math.sin(math.pow(math.fabs(input_point[i]), 0.5))
        result = 418.9829*dim - temp1
        if self.performance_mode_num == 2:
            threshold_value = 800
            if result < threshold_value:
                result = 0
            else:
                result = 1
        elif self.performance_mode_num == 3:
            threshold_value1 = 0
        elif self.performance_mode_num == 4:
            threshold_value1 = 400
            threshold_value2 = 800
            threshold_value3 = 1200
            if result < threshold_value1:
                result = 0
            elif threshold_value1 <= result < threshold_value2:
                result = 1
            elif threshold_value2 <= result < threshold_value3:
                result = 2
            elif result >= threshold_value3:
                result = 3
        return result

    # 2-d
    def benchmark5(self, input_point):
        dim = len(input_point)
        if dim == 2:
            x = input_point[0]
            y = input_point[1]
            temp1 = math.pow(math.pow(x, 2) + math.pow(y, 2), 0.5)/math.pi
            result = -math.fabs(math.sin(x)*math.cos(y)*math.exp(math.fabs(1 - temp1)))
            if self.performance_mode_num == 2:
                threshold_value = -6
                if result < threshold_value:
                    result = 0
                else:
                    result = 1
            elif self.performance_mode_num == 3:
                threshold_value1 = 0
            elif self.performance_mode_num == 4:
                threshold_value1 = -10
                threshold_value2 = -7
                threshold_value3 = -4
                if result < threshold_value1:
                    result = 0
                elif threshold_value1 <= result < threshold_value2:
                    result = 1
                elif threshold_value2 <= result < threshold_value3:
                    result = 2
                elif result >= threshold_value3:
                    result = 3
        else:
            result = -1
            print('**************The dimension is not supported***************')
        return result

    # 2-d
    def benchmark6(self, input_point):
        dim = len(input_point)
        if dim == 2:
            x = input_point[0]
            y = input_point[1]
            temp1 = math.pow(math.fabs(y - 0.01*math.pow(x, 2)), 0.5)
            result = 100*temp1 + 0.01*math.fabs(x + 10)
            if self.performance_mode_num == 2:
                threshold_value = 350
                if result < threshold_value:
                    result = 0
                else:
                    result = 1
            elif self.performance_mode_num == 3:
                threshold_value1 = 0
            elif self.performance_mode_num == 4:
                threshold_value1 = 100
                threshold_value2 = 200
                threshold_value3 = 300
                if result < threshold_value1:
                    result = 0
                elif threshold_value1 <= result < threshold_value2:
                    result = 1
                elif threshold_value2 <= result < threshold_value3:
                    result = 2
                elif result >= threshold_value3:
                    result = 3
        else:
            result = -1
            print('**************The dimension is not supported***************')
        return result

    # any dimension
    def benchmark7(self, input_point):
        dim = len(input_point)
        temp1 = 0
        for i in range(0, dim-1):
            w = 1 + (input_point[i]-1)/4
            temp1 = temp1 + math.pow(w-1, 2)*(1+10*math.pow(math.sin(math.pi*w+1), 2))
        w1 = 1 + (input_point[0] - 1)/4
        wd = 1 + (input_point[dim-1] - 1)/4
        result = math.pow(math.sin(math.pi*w1), 2) + temp1 + math.pow(wd-1, 2)*(1 + math.pow(math.sin(2*math.pi*wd), 2))
        if self.performance_mode_num == 2:
            threshold_value = 35
            if result < threshold_value:
                result = 0
            else:
                result = 1
        elif self.performance_mode_num == 3:
            threshold_value1 = 0
        elif self.performance_mode_num == 4:
            threshold_value1 = 15
            threshold_value2 = 28
            threshold_value3 = 38
            if result < threshold_value1:
                result = 0
            elif threshold_value1 <= result < threshold_value2:
                result = 1
            elif threshold_value2 <= result < threshold_value3:
                result = 2
            elif result >= threshold_value3:
                result = 3
        return result

    # 2-d
    def benchmark8(self, input_point):
        dim = len(input_point)
        if dim == 2:
            x = input_point[0]
            y = input_point[1]
            result = -math.cos(x)*math.cos(y)*math.exp(-math.pow(x-math.pi, 2) - math.pow(y-math.pi, 2))
            if self.performance_mode_num == 2:
                threshold_value = -0.1
                if result < threshold_value:
                    result = 0
                else:
                    result = 1
            elif self.performance_mode_num == 3:
                threshold_value1 = 0
            elif self.performance_mode_num == 4:
                threshold_value1 = -0.6
                threshold_value2 = -0.4
                threshold_value3 = -0.2
                if result < threshold_value1:
                    result = 0
                elif threshold_value1 <= result < threshold_value2:
                    result = 1
                elif threshold_value2 <= result < threshold_value3:
                    result = 2
                elif result >= threshold_value3:
                    result = 3
        else:
            result = -1
            print('**************The dimension is not supported***************')
        return result

    # any dimension
    def benchmark9(self, input_point):
        dim = len(input_point)
        temp1 = 0
        para_m = 10
        for i in range(0, dim):
            xi = input_point[i]
            temp1 = temp1 + math.sin(xi)*math.pow(math.sin((i+1)*math.pow(xi, 2)/math.pi), 2*para_m)
        result = -temp1
        if self.performance_mode_num == 2:
            threshold_value = 0.1
            if result < threshold_value:
                result = 0
            else:
                result = 1
        elif self.performance_mode_num == 3:
            threshold_value1 = 0
        elif self.performance_mode_num == 4:
            threshold_value1 = -0.5
            threshold_value2 = 0
            threshold_value3 = 0.5
            if result < threshold_value1:
                result = 0
            elif threshold_value1 <= result < threshold_value2:
                result = 1
            elif threshold_value2 <= result < threshold_value3:
                result = 2
            elif result >= threshold_value3:
                result = 3
        return result







