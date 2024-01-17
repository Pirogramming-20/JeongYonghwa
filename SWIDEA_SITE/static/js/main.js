function changeMarked(pk) {
    const mark = document.getElementById("mark_" + pk);
    fetch('/idea/change_marked/' + pk)
        .then((response) => response.json())
        .then((json) => {
            mark.innerText = json.marked ? "❤️" : "🤍";
        });
}

function decreaseInterest(pk) {
    const interest = document.getElementById("interest_" + pk);
    fetch('/idea/decrease_interest/' + pk)
        .then((response) => response.json())
        .then((json) => {
            interest.innerText = json.interest;
        });
}

function increaseInterest(pk) {
  const interest = document.getElementById("interest_" + pk);
  fetch("/idea/increase_interest/" + pk)
    .then((response) => response.json())
    .then((json) => {
      interest.innerText = json.interest;
    });
}

const criteria = document.getElementById("criteria");
if (criteria) {
    criteria.addEventListener("change", () => {
      var newUrl =
        window.location.href.split("/")[0] + "/idea/order/" + criteria.value + "?page=1";
        window.location.href = newUrl;
    });
}

const devtool_container = document.querySelector(".devtool-outter-container");
const devtool_search = document.getElementById("devtool-search");
if (devtool_container && devtool_search) {
    devtool_search.addEventListener("input", () => {
        // 입력값이 없을때 url처리가 넘어가지 않아 특수한 장치를 추가
        var input = devtool_search.value !== "" ? devtool_search.value : "__all";
        fetch('/devtool/search/' + input)
            .then((response) => response.json())
            .then((json) => {
                devtool_container.innerHTML = json.result;
            });
    });
}