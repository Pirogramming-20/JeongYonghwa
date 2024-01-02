//브라우저 API(fetch)를 이용해 JSON파일 참조
function loadItems() {
  return fetch("data/data.json")
    .then((response) => response.json())
    .then((json) => json.items);
  // response의 body를 json으로 변경 / json에서 원하는 부분만 다시 return
}

function displayItems(items) {
  const container = document.querySelector(".items");
  container.innerHTML = items.map((item) => createHTMLString(item)).join("");
}

function createHTMLString(item) {
  return `
    <li class="item">
      <img src="${item.image}" alt="${item.type}" class="item__thumbnail">
      <span class="item__description">${item.gender}, ${item.size}</span>
    </li>
    `;
}

function onButtonClick(event, items) {
  //앞서 정의한 data-key/value는
  // event > target > dataset에 key / value로 저장
  const dataset = event.target.dataset;
  const key = dataset.key;
  const value = dataset.value;

  if (key == null || value == null) {
    return;
  }

  // 일일이 html을 새로 삽입하지 않고 정보만 업데이트하는 방식
  updateItems(items, key, value);
}

function updateItems(items, key, value) {
  const actualItems = document.getElementsByClassName("item");
  for (let i = 0; i < items.length; i++) {
    if (items[i][key] === value) {
      actualItems[i].classList.remove("invisible");
    } else {
      actualItems[i].classList.add("invisible");
    }
  }
}

function setEventListeners(items) {
  const logo = document.querySelector(".logo");
  const buttons = document.querySelector(".buttons");
  logo.addEventListener("click", () => displayItems(items));
  buttons.addEventListener("click", (event) => onButtonClick(event, items));
}

loadItems()
  .then((items) => {
    displayItems(items);
    setEventListeners(items);
  })
  .catch(console.log);
