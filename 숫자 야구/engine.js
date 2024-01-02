function createResultDiv(display, nums, strike, ball) {

    const checkResultDiv = document.createElement('div');
    checkResultDiv.classList.add('check-result');

    const leftDiv = document.createElement('div');
    leftDiv.classList.add('left');
    leftDiv.innerText= nums;
    checkResultDiv.appendChild(leftDiv);

    const seperator = document.createElement('div');
    seperator.innerText = ':';
    checkResultDiv.appendChild(seperator);

    // strike + ball = 0 => Out

    const rightDiv = document.createElement('div');
    rightDiv.classList.add('right');

    if (strike + ball == 0) {
        const outMark = document.createElement('div');
        outMark.classList.add('out', 'num-result');
        outMark.innerText = 'O';
        rightDiv.appendChild(outMark);
        checkResultDiv.appendChild(rightDiv);
        display.appendChild(checkResultDiv);

        triesLeft--;
        checkTotalResult(triesLeft, strike);
        return;
    }
    const strikeCount = document.createElement('div');
    let strikeStr = ' ' + strike.toString() + ' ';
    strikeCount.innerText = strikeStr;
    strikeCount.style.display = "inline"
    rightDiv.appendChild(strikeCount);

    const strikeMark = document.createElement('div');
    strikeMark.classList.add('strike', 'num-result');
    strikeMark.innerText = 'S';
    rightDiv.appendChild(strikeMark);

    const ballCount = document.createElement('div');
    let ballStr = ' ' + ball.toString() + ' ';
    ballCount.innerText = ballStr;
    ballCount.style.display = "inline"
    rightDiv.appendChild(ballCount);

    const ballMark = document.createElement('div');
    ballMark.classList.add('ball', 'num-result');
    ballMark.innerText = 'B';
    rightDiv.appendChild(ballMark);

    checkResultDiv.appendChild(rightDiv);
    display.appendChild(checkResultDiv);

    triesLeft--;
    checkTotalResult(triesLeft, strike);
}

function checkTotalResult(curTry, strikeCount) {
    display.scrollTop = display.scrollHeight;
    if (strikeCount == 3) {
        const resultImage = document.getElementById('game-result-img');
        resultImage.setAttribute('src', './success.png');
        disableButton();
    } else if (!curTry) {
        const resultImage = document.getElementById('game-result-img');
        resultImage.setAttribute('src', './fail.png');
        disableButton();
    }  
}

function disableButton() {
    const submitBt = document.getElementsByClassName('submit-button');
    submitBt[0].disabled = true;
    submitBt[0].style.opacity = "0.5";
    submitBt[0].style.cursor = "default";
}

function checkResult(ranNums, inputNums) {
    let strikeCount = 0;
    let ballCount = 0;
    for (let i = 0; i < 3; i++) {
        if (ranNums[i] == inputNums[i]) {
            strikeCount++;
        } else if (ranNums.includes(parseInt(inputNums[i]))) {
            ballCount++;
        }
    }
    return {strike:strikeCount, ball:ballCount};
}

function check_numbers() {
    let num1 = document.getElementById('number1');
    let num2 = document.getElementById('number2');
    let num3 = document.getElementById('number3');
    const clearAll = () => {
        num1.value = '';
        num2.value = '';
        num3.value = '';
    } 
    if (num1.value==''||num2.value==''||num3.value=='') {
        return clearAll();
    } else if (num1.value==num2.value||num2.value==num3.value||num3.value==num1.value) {
        return clearAll();
    } // 중복된 숫자 입력 방지
    let inputNums = [num1.value,num2.value,num3.value];
    let result = checkResult(numbers, inputNums);
    let numToStr = inputNums.join(' ');
    clearAll();
    return createResultDiv(display, numToStr, result.strike, result.ball);
}

// 게임의 메인(한번만 실행)
let numbers = [];
let display = document.querySelector('.result-display');

let triesLeft = 9;

while (numbers.length < 3) {
    const number = Math.floor(Math.random() * 9) + 1;

    if (!numbers.includes(number)) {
        numbers.push(number); 
    }
}
console.log(numbers);