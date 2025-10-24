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

// Dropdown Menu
let dropdownMenuItemTitles = document.querySelectorAll('.dropdown-menu-item-title');

dropdownMenuItemTitles.forEach(menuItemTitle => {
    menuItemTitle.addEventListener('click', (e) => {

        const menuItemData = e.target.nextElementSibling;

        menuItemData.style.setProperty('--openHeight', menuItemData.scrollHeight + 'px');
    
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

menuElements.forEach(menuElement => {
    
    menuElement.addEventListener('mouseover', showAreaInfo);
    menuElement.addEventListener('mouseout', hideAreaInfo);
});

const areaInfoDisplay = document.getElementById('info-image');

areaInfoDisplay.addEventListener('mouseover', showAreaInfo);
areaInfoDisplay.addEventListener('mouseout', hideAreaInfo);

function showAreaInfo(e) {

    const menuElement = e.target;

    var name = menuElement.firstChild.innerHTML;
    var area = menuElement.parentElement.parentElement.parentElement.parentElement.parentElement.previousElementSibling.innerHTML.replaceAll(" ", "_").replaceAll("'", "").toLowerCase();
    name = name.replaceAll(" ", "_").replaceAll('(', '').replaceAll(')', '').replaceAll("'", "").toLowerCase();
    var path = area.concat("/").concat(name).concat(".png");

    const x = menuElement.getBoundingClientRect().x + menuElement.getBoundingClientRect().width - areaInfoDisplay.getBoundingClientRect().width / 1.5;
    const y = menuElement.getBoundingClientRect().y + (menuElement.getBoundingClientRect().height / 2 - areaInfoDisplay.getBoundingClientRect().height / 2 + window.scrollY);

    areaInfoDisplay.style.backgroundImage = "url(img/info/" + path + ")";
    areaInfoDisplay.style.left = x + 'px';
    areaInfoDisplay.style.top = y + 'px';
    areaInfoDisplay.style.opacity = 1;

}

function hideAreaInfo() {

    areaInfoDisplay.style.opacity = 0;

}


//pyodide
let pyodide;

function downloadFile(filename) {
        let data = pyodide.FS.readFile(filename, { encoding: "utf8" });
        let blob = new Blob([data], { type: "text/plain" });
        let link = document.createElement("a");
        link.href = URL.createObjectURL(blob);
        link.download = filename;
        link.click();
}

async function initPyodide() {
    // Pyodide laden
    pyodide = await loadPyodide();

    const pyFiles = ["python/data.py", "python/init.py", "python/writing.py", "python/main.py"];

    //load files
    async function addFile(filename) {
        let response = await fetch(filename);
        let code = await response.text();
        pyodide.FS.writeFile(filename.split("/").pop(), code);
    }

    for (let file of pyFiles) {
        await addFile(file);
    }
}

async function runMain() {
    // refresh main and init
    await pyodide.runPythonAsync(`
        import sys
        for mod in ["main", "init"]:
            sys.modules.pop(mod, None)
        `);
    
    // rewrite init file
    pyodide.FS.writeFile("init.py", setInit());

    //execute
    await pyodide.runPythonAsync(`import main`);

    downloadFile(pyodide.FS.readdir(".")[pyodide.FS.readdir(".").length - 1]);
}

initPyodide()