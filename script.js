window.addEventListener('pagehide', () => {
    pyodide = null;
    pyodideLoading = null;
});

const init_checks = document.getElementsByClassName("inits");

function generateSeed() {
    document.getElementById("seed-input").value = Math.floor(Math.random() * 10000000000000000);
}

function capitalize(val) {
    return String(val).charAt(0).toUpperCase() + String(val).slice(1);
}

function setInit() {
    let initCode = "";
    let seed = document.getElementById("seed-input");
    if (seed.value == "") {
        generateSeed()
    }
    initCode = initCode.concat("seed = ").concat(String(seed.value));
    initCode = initCode.concat("\norb_bundle_size = ").concat(String(orb_bundle_size));
    for (let i = 0; i < init_checks.length; i++) {
       initCode = initCode.concat("\n").concat(init_checks[i].name.concat(" = ").concat(capitalize(init_checks[i].checked)));
    }
    return initCode;
}

const scrollBarWidth = window.innerWidth - document.documentElement.clientWidth;
document.getElementById("orb-checkbox").addEventListener("click", function() {
    document.getElementById("alert-box").style.display = "block";
    document.body.classList.add("locked");
}, { once: true });
function closeAlert() {
    document.getElementById("alert-box").style.display = "none";
    document.body.classList.remove("locked");
}

// Slider
const slider = document.getElementById('slider');
const sliderBar = document.getElementById('slider-bar');
const sliderContainer = document.getElementById('slider-container');
const sliderCircles = document.getElementsByClassName('slider-circle');
function clickedOrbs() {
    sliderContainer.classList.toggle('disable-slider');
}

const orbsSteps = [1, 5, 10, 25, 50]
slider.setAttribute('max', orbsSteps.length - 1);
slider.value = Math.floor(orbsSteps.length / 2);
sliderBar.style.width = String(slider.value) * (95 / (orbsSteps.length - 1)) + "%";
var orb_bundle_size = orbsSteps[parseInt(slider.value)];
function changeSlider(e) {
    orb_bundle_size = orbsSteps[parseInt(e.value)];

    sliderBar.style.width = String(e.value * (95 / (orbsSteps.length - 1))) + "%";
    for (let i = 0; i < sliderCircles.length; i++) {
        if (i < e.value) {
           sliderCircles[i].classList.remove('circle-inactive');
        } else {
            sliderCircles[i].classList.add('circle-inactive');
        }
    }
}

// Images Loading
const imageCache = new Map();

function preloadImage(src) {
    if (imageCache.has(src)) return;

    const img = new Image();
    img.src = src;

    imageCache.set(src, img);
}

// Dropdown Menu
let dropdownMenuItemTitles = document.querySelectorAll('.dropdown-menu-item-title');

dropdownMenuItemTitles.forEach(menuItemTitle => {
    menuItemTitle.addEventListener('click', (e) => {

        const menuItemData = e.target.nextElementSibling;

        const height = menuItemData.scrollHeight;

        // Set Srat Value
        menuItemData.style.setProperty('--openHeight', '0px');

        // Force Reflow
        void menuItemData.offsetHeight;

        // Animate
        requestAnimationFrame(() => {
            menuItemData.style.setProperty(
                '--openHeight',
                `${height}px`
            );
        });
    
        menuItemData.classList.toggle('show');
        menuItemData.classList.toggle('hide');
        
        const parent = menuItemData.parentElement.parentElement.parentElement;
        const parentScrollHeight = parent.scrollHeight;
        
        if (parent.nodeName == 'DD') {
            
            var scrollHeight = 0;
            
            for (let i = 0; i < dropdownMenuItemTitles.length; i++) {
                
                var curItem = dropdownMenuItemTitles[i].nextElementSibling;
                if (curItem.classList.contains('show') && curItem.previousElementSibling.classList.contains("sub") && curItem != menuItemData) {
                    curItem.style.setProperty('--openHeight', curItem.scrollHeight + 'px');
                    scrollHeight = scrollHeight - curItem.scrollHeight;
                    curItem.classList.toggle('show');
                    curItem.classList.toggle('hide');
                }
            }
            if (menuItemData.classList.contains("show")) {
                scrollHeight = scrollHeight + menuItemData.scrollHeight;
            } else {
                scrollHeight = scrollHeight - menuItemData.scrollHeight;
            }
            
            parent.style.setProperty('--openHeight', parentScrollHeight + scrollHeight + 'px');
        }
        if (parent.nodeName == 'DIV') {
            for (let i = 0; i < dropdownMenuItemTitles.length; i++) {
                
                var curItem = dropdownMenuItemTitles[i].nextElementSibling;
                if (curItem.classList.contains('show') && curItem != menuItemData) {
                    curItem.style.setProperty('--openHeight', curItem.scrollHeight + 'px');
                    curItem.classList.toggle('show');
                    curItem.classList.toggle('hide');
                }
            }
        }
    })
});

// Show Images
const menuElements = document.querySelectorAll('.dropdown-submenu-item');

document.addEventListener('mouseover', (e) => {
    const menuElement = e.target.closest('.dropdown-submenu-item');

    if (!menuElement) return;

    showAreaInfo(menuElement);
});

document.addEventListener('mouseout', (e) => {
    if (e.target.closest('.dropdown-submenu-item')) {
        hideAreaInfo();
    }
});

const areaInfoDisplay = document.getElementById('info-image');

areaInfoDisplay.addEventListener('mouseover', showAreaInfo);
areaInfoDisplay.addEventListener('mouseout', hideAreaInfo);

function showAreaInfo(menuElement) {

    var area = menuElement.parentElement.parentElement.parentElement.parentElement.parentElement.previousElementSibling.innerText;
    area = area.replaceAll(" ", "_").replaceAll("'", "").toLowerCase();
    var name = menuElement.firstChild.innerHTML;
    name = name.replaceAll(" ", "_").replaceAll('(', '').replaceAll(')', '').replaceAll("'", "").toLowerCase().concat(".webp");
    let path = area + "/" + name;

    const x = menuElement.getBoundingClientRect().x + menuElement.getBoundingClientRect().width - areaInfoDisplay.getBoundingClientRect().width / 1.5;
    const y = menuElement.getBoundingClientRect().y + (menuElement.getBoundingClientRect().height / 2 - areaInfoDisplay.getBoundingClientRect().height / 2 + window.scrollY);

    const imageSrc = `img/info/${path}`;
    preloadImage(imageSrc);


    areaInfoDisplay.style.backgroundImage = `url(${imageSrc})`;
    areaInfoDisplay.style.left = x + 'px';
    areaInfoDisplay.style.top = y + 'px';
    areaInfoDisplay.style.opacity = 1;

}

function hideAreaInfo() {

    areaInfoDisplay.style.opacity = 0;

}


// Pyodide
let pyodide = null;
let pyodideLoading = null;
let lastGeneratedFile = null;

const delay = ms => new Promise(res => setTimeout(res, ms));
const fileButtons = document.getElementsByClassName("fileButton");

async function loadPyodideRuntime() {
    if (pyodide) return pyodide;
    if (pyodideLoading) return pyodideLoading;

    pyodideLoading = (async () => {
        pyodide = await loadPyodide();
        const pyFiles = [
            "python/data.py",
            "python/init.py",
            "python/writing.py",
            "python/main.py"
        ];
        await Promise.all(pyFiles.map(async (filename) => {
            const response = await fetch(filename);
            const code = await response.text();
            pyodide.FS.writeFile(filename.split("/").pop(), code);
        }));
        return pyodide;
    })();
    return pyodideLoading;
}

async function runMain() {
    const button = document.getElementById("btn");
    try {
        button.classList.add("disabled");
        fileButtons[0].classList.add("disabled");
        fileButtons[1].classList.add("disabled");
        button.textContent = "Loading...";
        await loadPyodideRuntime();
        
        button.textContent = "Generating...";
        await delay(600);
        await pyodide.runPythonAsync(`
            import sys
            for mod in ["main", "init"]:
                sys.modules.pop(mod, None)
        `);
        
        pyodide.FS.writeFile("init.py", setInit());
        await pyodide.runPythonAsync(`import main`);
        
        const files = pyodide.FS.readdir(".");
        lastGeneratedFile = files[files.length - 1]; 
        
    } catch (err) {
        console.error(err);
        alert("Error while generating Splits.\n\nPlease try again using a different seed.\nIf the error persists please message me.");
    } finally {
        button.classList.remove("disabled");
        fileButtons[0].classList.remove("disabled");
        fileButtons[1].classList.remove("disabled");
        button.textContent = "Generate New Splits";
    }
}

function getFileData(filename) {
    if (!pyodide || !filename) {
        return null;
    }
    const data = pyodide.FS.readFile(filename); 
    return new Blob([data], { type: "text/plain;charset=utf-8" });
}

function downloadFile() {
    const blob = getFileData(lastGeneratedFile);
    if (!blob) return;

    const link = document.createElement("a");
    link.href = URL.createObjectURL(blob);
    link.download = lastGeneratedFile;
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(link.href);
}

function openFileInNewTab() {
    const blob = getFileData(lastGeneratedFile);
    if (!blob) return;

    const fileURL = URL.createObjectURL(blob);
    const newTab = window.open(fileURL, '_blank', 'noopener,noreferrer');

    setTimeout(() => {
        URL.revokeObjectURL(fileURL);
    }, 1000);
}