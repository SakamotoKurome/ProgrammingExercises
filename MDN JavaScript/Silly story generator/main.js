const customName = document.getElementById('customname');
const randomize = document.querySelector('.randomize');
const story = document.querySelector('.story');

function randomValueFromArray(array) {
    return array[Math.floor(Math.random() * array.length)];
}

// 千克转磅
function kg2b(value) {
    return value * 2.2046
}

// 摄氏度转华氏度
function c2f(C) {
    return 9 / 5 * C + 32
}

storyText = '今天气温 34 摄氏度，:inserta:出去遛弯。\
            当走到:insertb:门前时，突然就:insertc:。\
            人们都惊呆了，李雷全程目睹但并没有慌，\
            因为:inserta:是一个 130 公斤的胖子，天气又辣么热。'

insertX = ['怪兽威利', '大老爹', '圣诞老人']
insertY = ['肯德基', '迪士尼乐园', '白宫']
insertZ = ['自燃了', '在人行道化成了一坨泥', '变成一条鼻涕虫爬走了']

randomize.addEventListener('click', result);

function result() {
    let newStory = storyText;
    xItem = randomValueFromArray(insertX)
    yItem = randomValueFromArray(insertY)
    zItem = randomValueFromArray(insertZ)
    newStory = newStory.replace(':inserta:', xItem)
    newStory = newStory.replace(':inserta:', xItem)
    newStory = newStory.replace(':insertb:', yItem)
    newStory = newStory.replace(':insertc:', zItem)


    if (customName.value !== '') {
        let name = customName.value;
        newStory = newStory.replace('李雷', name)

    }

    if (document.getElementById("american").checked) {

        let weight = Math.round(kg2b(130));
        let temperature = Math.round(c2f(34));
        weight += ' 磅'
        temperature += ' 华氏度'
        newStory = newStory.replace('130 公斤', weight)
        newStory = newStory.replace('34 摄氏度', temperature)
    }

    story.textContent = newStory;
    story.style.visibility = 'visible';
}