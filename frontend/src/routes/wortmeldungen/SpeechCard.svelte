<script>
	export let speech = null;

  
	const mapLabelsToBackgroundColor = (labelName) => {
		labelName = labelName.toLowerCase();
    // we neet to use the full string tailwind classes, so the preprocessor will pick this up correctly
		let colorDict = {
			"contra": "bg-[#F7464A]",
			"pro": "bg-[#68E08C]",
			"erste lesung": "bg-[#949FB1]",
			"regierungsbank": "bg-[#4D5360]",
			"tatsächliche berichtigung": "#bg-[FDB45C]",
			"ap" : "bg-[#46BFBD]", 
			"aktuelle stunde" : "bg-[#68bce0]",
			"begründung" : "bg-[#e068bc]",
			"berichterstattung ausschuss" : "bg-[#e08c68]", 
			"dringliche anfrage" : "bg-[#e894c3]",
			"dringlicher (entschließungs-)antrag" : "bg-[#b994e8]",
			"erklärung" : "bg-[#94e8b9]", 
			"erwiderung" : "bg-[#c3e894]",
			"europäische union" : "#bg-[df6a71]",
			"wortmeldung zur geschäftsbehandlung": "bg-[#e89499]",
			"kurze debatte" : "bg-[#f6d3d5]",
			"rf" : "bg-[#7f85e3]",  
			"regierungsbank staatssekretär:in" : "bg-[#d3d5f6]",
			"regierungsvorlage" : "bg-[#6adfd8]",
			"unterzeichner:in" : "bg-[#d3f6f3]",
			"wahldebatte" : "bg-[#df6a71]",
			"wortmeldung" : "bg-[#f1bec1]",
		}
		return colorDict[labelName];
	};
</script>

<div class="card min-w-fit max-w-xs {mapLabelsToBackgroundColor(speech.typeOfSpeech)} shadow-xl">
    <div class="card-body"> 
        <h2 class="card-title self-center">{speech.nameOfSpeaker}</h2>
        <div class="relative flex items-center">
            <div class="flex-grow border-t border-gray-400"></div>
            <span class="flex-shrink mx-4 text-gray-400">{speech.politicalPartie}</span>
            <div class="flex-grow border-t border-gray-400"></div>
        </div> 
       
      <p class="text-justify"> [..] das ist nur ein platzhalter [..]</p>

        <div class="flex flex-wrap self-center gap-2">
            <div class="badge badge-outline">{speech.typeOfSpeech}</div>
            <div class="badge badge-outline">{speech.lengthOfSpeechInSec} min</div>        
          </div>
    </div>
</div>