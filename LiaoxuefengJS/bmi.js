const height = parseFloat(prompt('请输入身高(m):'));
const weight = parseFloat(prompt('请输入体重(kg):'));
const bmi = weight / (height * height);
if (bmi < 18.5) {
    alert(bmi + ' 过轻')
} else if (bmi >= 18.5 && bmi < 25) {
    alert(bmi + ' 正常')
} else if (bmi >= 25 && bmi < 28) {
    alert(bmi + ' 过重')
} else if (bmi >= 28 && bmi < 32) {
    alert(bmi + ' 肥胖')
} else if (bmi >= 32) {
    alert(bmi + ' 严重肥胖')
}