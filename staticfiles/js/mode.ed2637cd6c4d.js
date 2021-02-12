var setTheme = localStorage.getItem('theme')
console.log('theme:', setTheme)

	if (setTheme == null) {
	    swapStyle('styles.css')
	}else{
	    swapStyle(setTheme)
	}

function swapStyle(sheet){
    document.getElementById('mystylesheet').href = sheet
    localStorage.setItem('theme', sheet)
}


/*AJaxify*/
