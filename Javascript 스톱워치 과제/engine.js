const curTime = document.getElementById("currentTime");
const startBtn = document.getElementById("startBtn");
const stopBtn = document.getElementById("stopBtn");
const resetBtn = document.getElementById("resetBtn");
const recordBox = document.getElementById("recordBox");
const deleteBtn = document.getElementById("delete");
const selectAllBtn = document.getElementById("selectAll");

let sec = 0;
let millSec = 0;
let counter;
let checkboxList = [];

function updateTime() {
  millSec += 1;
  if (millSec == 100) {
    sec += 1;
    millSec = 0;
  }
  curTime.innerText =
    sec.toString().padStart(2, "0") + ":" + millSec.toString().padStart(2, "0");
}

function addRecord() {
  const recordContainer = document.createElement("div");
  const checkbox = document.createElement("input");
  const time = document.createElement("span");

  checkbox.addEventListener("click", () => {
    const items = document.getElementsByClassName("selectItem");
    if (checkbox.checked) {
      const allChecked = Array.from(items).every(
        (inputBox) => inputBox.checked
      );
      if (!allChecked) {
        return;
      }
      selectAllBtn.checked = true;
    } else {
      const allUnchecked = Array.from(items).every(
        (inputBox) => !inputBox.checked
      );
      if (allUnchecked) {
        return;
      }
      selectAllBtn.checked = false;
    }
  });

  recordContainer.classList.add("recordContainer");
  checkbox.classList.add("selectItem");
  checkbox.setAttribute("type", "checkbox");

  time.innerText =
    sec.toString().padStart(2, "0") + ":" + millSec.toString().padStart(2, "0");

  recordContainer.appendChild(checkbox);
  recordContainer.appendChild(time);

  recordBox.appendChild(recordContainer);
}

startBtn.addEventListener("click", () => {
  // 중복 클릭으로 인해 counter가 여러 개 생기는 것을 방지
  if (counter) {
    return;
  }
  counter = setInterval(updateTime, 10);
});

stopBtn.addEventListener("click", () => {
  clearInterval(counter);
  counter = null;
  addRecord();
});

resetBtn.addEventListener("click", () => {
  clearInterval(counter);
  counter = null;
  sec = 0;
  millSec = 0;
  curTime.innerText = "00:00";
});

deleteBtn.addEventListener("click", () => {
  const items = document.getElementsByClassName("recordContainer");
  Array.from(items).forEach((container) => {
    let inputBox = container.getElementsByClassName("selectItem")[0];
    if (inputBox.checked) {
      recordBox.removeChild(container);
    }
    selectAllBtn.checked = false;
  });
});

selectAllBtn.addEventListener("click", () => {
  const items = document.getElementsByClassName("selectItem");
  Array.from(items).forEach((inputBox) => {
    if (selectAllBtn.checked && !inputBox.checked) {
      inputBox.checked = true;
    } else if (!selectAllBtn.checked && inputBox.checked) {
      inputBox.checked = false;
    }
  });
});
