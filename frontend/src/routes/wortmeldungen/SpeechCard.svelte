<script>
	export let speech = null;

  
	const mapLabelsToBackgroundColor = (labelName) => {
		labelName = labelName.toLowerCase();
    // we neet to use the full string tailwind classes, so the preprocessor will pick this up correctly
		let colorDict = {
			"contra": "bg-red-50",
			"pro": "bg-green-50",
			"erste lesung": "bg-neutral-200",
			"regierungsbank": "bg-slate-100",
			"tatsächliche berichtigung": "bg-orange-200",
			"ap" : "bg-teal-50", 
			"aktuelle stunde" : "bg-cyan-100",
			"begründung" : "bg-pink-200",
			"berichterstattung ausschuss" : "bg-amber-600", 
			"dringliche anfrage" : "bg-fuchsia-400",
			"dringlicher (entschließungs-)antrag" : "bg-purple-300",
			"erklärung" : "bg-emerald-100", 
			"erwiderung" : "bg-lime-100",
			"europäische union" : "bg-red-800",
			"wortmeldung zur geschäftsbehandlung": "bg-yellow-900",
			"kurze debatte" : "bg-violet-400",
			"rf" : "bg-indigo-300",  
			"regierungsbank staatssekretär:in" : "bg-blue-50",
			"regierungsvorlage" : "bg-cyan-400",
			"unterzeichner:in" : "bg-indigo-50",
			"wahldebatte" : "bg-rose-500",
			"wortmeldung" : "bg-rose-50",
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