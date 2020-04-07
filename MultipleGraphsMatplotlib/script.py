import codecademylib
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]
middle_school_c = [78, 81, 71, 80, 89]


def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]
school_a_x = [0.8, 2.8, 4.8, 6.8, 8.8]
school_b_x = [1.6, 3.6, 5.6, 7.6, 9.6]
school_c_x = [2.4, 4.4, 6.4, 8.4, 10.4]
# Make your chart here
school_a_x = create_x(3, .8, 1, 5)
school_b_x = create_x(3, .8, 2, 5)
school_c_x = create_x(3, .8, 3, 5)

plt.figure(figsize=(10,8))
ax = plt.subplot()
plt.bar(school_a_x, middle_school_a)
plt.bar(school_b_x, middle_school_b, color='gray')
plt.bar(school_c_x, middle_school_c, color='purple')
middle_x = school_b_x
ax.set_xticks(school_b_x)
ax.set_xticklabels(unit_topics)
plt.legend(['Middle School A', 'Middle School B'], loc=1)
plt.title('Test Averages on Different Units')
plt.xlabel('Unit')
plt.ylabel('Test Average')
plt.axis([0, 12, 70, 90])
plt.savefig('my_side_by_side.png')
plt.show()