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
    for (let i = 0; i < init_checks.length; i++) {
       initCode = initCode.concat("\n").concat(init_checks[i].name.concat(" = ").concat(capitalize(init_checks[i].checked)));
    }
    return initCode;
}

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

        // Startwert setzen
        menuItemData.style.setProperty('--openHeight', '0px');

        // Reflow erzwingen
        void menuItemData.offsetHeight;

        // Danach animieren
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
            
            for (i = 0; i < dropdownMenuItemTitles.length; i++) {
                
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
            for (i = 0; i < dropdownMenuItemTitles.length; i++) {
                
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

// images
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
    console.log(area);
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


//pyodide
let pyodide = null;
let pyodideLoading = null;

async function loadPyodideRuntime() {
    if (pyodide) return pyodide;

    if (pyodideLoading) {
        return pyodideLoading;
    }

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

            pyodide.FS.writeFile(
                filename.split("/").pop(),
                code
            );
        }));

        return pyodide;
    })();

    return pyodideLoading;
}

function downloadFile(filename) {
    const data = pyodide.FS.readFile(filename, {
        encoding: "utf8"
    });

    const blob = new Blob([data], {
        type: "text/plain"
    });

    const link = document.createElement("a");

    link.href = URL.createObjectURL(blob);
    link.download = filename;

    document.body.appendChild(link);
    link.click();
    link.remove();

    URL.revokeObjectURL(link.href);
}

async function runMain() {
    const button = document.getElementById("btn");

    try {
        button.disabled = true;
        button.textContent = "Loading Pyodide...";

        await loadPyodideRuntime();

        button.textContent = "Generating...";

        await pyodide.runPythonAsync(`
            import sys
            for mod in ["main", "init"]:
                sys.modules.pop(mod, None)
        `);

        pyodide.FS.writeFile(
            "init.py",
            setInit()
        );

        await pyodide.runPythonAsync(`import main`);

        const files = pyodide.FS.readdir(".");
        downloadFile(files[files.length - 1]);

    } catch (err) {
        console.error(err);
        alert("Failed to generate splits.");

    } finally {
        button.disabled = false;
        button.textContent = "Generate Splits";
    }
}