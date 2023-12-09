<script>
	export let speech = null;
	export let legislature = null;
	export let meetingNr = null;
	export let topic = null;
	const getLongNameOfPoliticalParty = (shortName) => {
		let mapDict = {
			v: 'ÖVP',
			s: 'SPÖ',
			f: 'FPÖ',
			g: 'GRÜNE',
			n: 'NEOS'
		};
		let abbrToLower = shortName.toLowerCase();
		return mapDict[abbrToLower] ?? shortName;
	};

	const convertLengthToReadableString = (lengthInSec) => {
		const zeroPad = (num, places) => String(num).padStart(places, '0');
		let sec = zeroPad(lengthInSec % 60, 2);
		let min = Math.trunc(lengthInSec / 60);

		if (sec == 0) {
			return `${min}`;
		} else {
			return `${min}:${sec}`;
		}
	};
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
		};
		return colorDict[labelName];
	};
</script>

<div class="card max-w-xs {mapLabelsToBackgroundColor(speech.typeOfSpeech)} shadow-xl">
	<div class="card-body">
		<h2 class="card-title self-center">{speech.nameOfSpeaker}</h2>
		<div class="relative flex items-center">
			<div class="flex-grow border-t border-neutral" />
			<span class="flex-shrink mx-4 text-neutral truncate"
				>{speech.typeOfSpeech}</span
			>
			<div class="flex-grow border-t border-neutral" />
		</div>		
			{#if speech.speechSneakPeak != null}
				<p class="text-justify line-clamp-4">
					{speech.speechSneakPeak}
				</p>
				<a href="/wortmeldung/{legislature}/{meetingNr}/{encodeURIComponent(topic)}/{speech.speechNrInDebate}?speaker={speech.nameOfSpeaker}" class="btn btn-ghost">
					weiterlesen
				</a>
			{/if}
		
		<div class="flex flex-wrap self-center gap-2">
			<div class="badge badge-outline">{getLongNameOfPoliticalParty(speech.politicalPartie)}</div>			
			<div class="badge badge-outline">
				{convertLengthToReadableString(speech.lengthOfSpeechInSec)} min
			</div>
			{#if "applause" in speech?.activitiesCount}
				<div class="badge badge-outline">
					<div class="tooltip" data-tip="Beifall">
					👏🏻 {speech?.activitiesCount["applause"]}
					</div>
				</div>
			{/if}
			{#if "cheerfulness" in speech?.activitiesCount}
				<div class="badge badge-outline">
					<div class="tooltip" data-tip="Heiterkeit">
						😅 {speech?.activitiesCount["cheerfulness"]}
					</div>
				</div>
			{/if}
			{#if "shouting" in speech?.activitiesCount}
				<div class="badge badge-outline">
					<div class="tooltip" data-tip="Zwischenruf">
						🗣️ {speech?.activitiesCount["shouting"]}
					</div>
				</div>
			{/if}
		</div>
	</div>
</div>
