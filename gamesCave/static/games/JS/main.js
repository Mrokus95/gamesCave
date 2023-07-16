const carousel1Prev = document.querySelector("#carousel1 .prev");
const carousel1Next = document.querySelector("#carousel1 .next");
const carousel1Track = document.querySelector("#carousel1 .track");
const carousel1CardContainer = document.querySelectorAll(
	"#carousel1 .my-card-container"
);
const carousel1CardWidth = carousel1CardContainer[0].offsetWidth;
const carousel1VisibleCards = 5;
const carousel1TrackWidth = carousel1CardWidth * carousel1CardContainer.length;
let carousel1Position = 0;

// Klonowanie pierwszych widocznych kart dla carousel1
for (let i = 0; i < carousel1VisibleCards; i++) {
	carousel1Track.appendChild(carousel1CardContainer[i].cloneNode(true));
}

// Ustawianie szerokości kontenera .track dla carousel1
carousel1Track.style.width = `${carousel1TrackWidth}px`;

carousel1Next.addEventListener("click", () => {
	carousel1Position -= carousel1CardWidth;
	carousel1Track.style.transform = `translateX(${carousel1Position}px)`;

	// Przenoszenie pierwszego elementu na koniec listy dla carousel1
	const firstCard = carousel1Track.querySelector(".my-card-container");
	carousel1Track.appendChild(firstCard.cloneNode(true));
	carousel1Track.removeChild(firstCard);

	// Aktualizacja pozycji dla carousel1
	carousel1Position += carousel1CardWidth;
	carousel1Track.style.transform = `translateX(${carousel1Position}px)`;
});

carousel1Prev.addEventListener("click", () => {
	carousel1Position += carousel1CardWidth;
	carousel1Track.style.transform = `translateX(${carousel1Position}px)`;

	// Przenoszenie ostatniego elementu na początek listy dla carousel1
	const lastCard = carousel1Track.lastElementChild;
	carousel1Track.insertBefore(
		lastCard.cloneNode(true),
		carousel1Track.firstChild
	);
	carousel1Track.removeChild(lastCard);

	// Aktualizacja pozycji dla carousel1
	carousel1Position -= carousel1CardWidth;
	carousel1Track.style.transform = `translateX(${carousel1Position}px)`;
});

const carousel2Prev = document.querySelector("#carousel2 .prev");
const carousel2Next = document.querySelector("#carousel2 .next");
const carousel2Track = document.querySelector("#carousel2 .track");
const carousel2CardContainer = document.querySelectorAll(
	"#carousel2 .my-card-container"
);
const carousel2CardWidth = carousel2CardContainer[0].offsetWidth;
const carousel2VisibleCards = 5;
const carousel2TrackWidth = carousel2CardWidth * carousel2CardContainer.length;
let carousel2Position = 0;

// Klonowanie pierwszych widocznych kart dla carousel2
for (let i = 0; i < carousel2VisibleCards; i++) {
	carousel2Track.appendChild(carousel2CardContainer[i].cloneNode(true));
}

// Ustawianie szerokości kontenera .track dla carousel2
carousel2Track.style.width = `${carousel2TrackWidth}px`;

carousel2Next.addEventListener("click", () => {
	carousel2Position -= carousel2CardWidth;
	carousel2Track.style.transform = `translateX(${carousel2Position}px)`;

	// Przenoszenie pierwszego elementu na koniec listy dla carousel2
	const firstCard = carousel2Track.querySelector(".my-card-container");
	carousel2Track.appendChild(firstCard.cloneNode(true));
	carousel2Track.removeChild(firstCard);

	// Aktualizacja pozycji dla carousel2
	carousel2Position += carousel2CardWidth;
	carousel2Track.style.transform = `translateX(${carousel2Position}px)`;
});

carousel2Prev.addEventListener("click", () => {
	carousel2Position += carousel2CardWidth;
	carousel2Track.style.transform = `translateX(${carousel2Position}px)`;

	// Przenoszenie ostatniego elementu na początek listy dla carousel2
	const lastCard = carousel2Track.lastElementChild;
	carousel2Track.insertBefore(
		lastCard.cloneNode(true),
		carousel2Track.firstChild
	);
	carousel2Track.removeChild(lastCard);

	// Aktualizacja pozycji dla carousel2
	carousel2Position -= carousel2CardWidth;
	carousel2Track.style.transform = `translateX(${carousel2Position}px)`;
});

// Messages

const introElement = document.getElementById("error");

introElement.addEventListener("animationend", () => {
    introElement.style.display = "none";
});
