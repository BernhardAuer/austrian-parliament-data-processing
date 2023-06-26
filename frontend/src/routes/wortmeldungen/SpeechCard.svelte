<script>
	export let speech = null;
</script>

<div class="card min-w-fit max-w-xs bg-green-50 shadow-xl">
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
            <div class="badge badge-outline">{speech.lengthOfSpeechInSec} sec</div>        
          </div>
    </div>
</div>