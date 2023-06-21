<script>
	import AutoComplete from 'simple-svelte-autocomplete';
	import ChartService from './../services/chartService.js';
	import { scrollIntoView } from 'seamless-scroll-polyfill';

	export let selectedFilterOptions = null;

	let rerenderTrigger = 0;
	let service = new ChartService(); // todo: svelte DI

	const resetAutoCompleter = () => {
		selectedFilterOptions.topic = null;
		rerenderTrigger = rerenderTrigger + 1;
	};

	const scrollAutoCompleteToTop = () => {
		scrollIntoView(document.getElementById('topic'), {
			behavior: 'smooth',
			block: 'start',
			inline: 'nearest'
		});
	};

	// subscribing ONLY to properties is not possible, so we use this workaround
	$: selectedLegislature = selectedFilterOptions.legislature;
	$: selectedMeetingNumber = selectedFilterOptions.meetingNumber;
	$: selectedLegislature, selectedMeetingNumber, resetAutoCompleter();
</script>

<div class="testparent w-full relative">
	<label class="block text-gray-700 text-sm font-bold mb-2" for="topic">Thema:</label>
	<div
		class="tooltip tooltip-left absolute top-0 right-0"
		data-tip="Die Suche nach Themen berücksichtigt die ausgewählte Gesetzgebungsperiode und Sitzung."
	>
		<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5">
			<path
				fill-rule="evenodd"
				d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a.75.75 0 000 1.5h.253a.25.25 0 01.244.304l-.459 2.066A1.75 1.75 0 0010.747 15H11a.75.75 0 000-1.5h-.253a.25.25 0 01-.244-.304l.459-2.066A1.75 1.75 0 009.253 9H9z"
				clip-rule="evenodd"
			/>
		</svg>
	</div>
	{#key rerenderTrigger}
		<AutoComplete
			onFocus={scrollAutoCompleteToTop}
			minCharactersToSearch="0"
			placeholder="Suche Themen"
			hideArrow="true"
			inputClassName="w-full text-base"
			className="input input-bordered w-full text-base"
			noInputStyles="false"
			showClear="true"
			lock="false"
			noResultsText="Kein Suchergebnis gefunden. Geben Sie bitte vollständige Wörter ein"
			loadingText="Lade Ergebnisse..."
			searchFunction={(keyword) =>
				service.searchTopics(
					keyword,
					selectedFilterOptions.legislature,
					selectedFilterOptions.meetingNumber
				)}
			bind:selectedItem={selectedFilterOptions.topic}
			labelFunction={(selected) => {
				let labelText = '';
				if (selected?.topNr != null) {
					labelText = labelText + selected.topNr + ': ';
				}
				labelText = labelText + selected.topic;
				return labelText;
			}}
			inputId="topic"
			name="Themensuche"
		/>
	{/key}
</div>

<style>
	/* this is a hack ... please help me fixing */
	.testparent :global(.autocomplete) {
		padding-top: 0.7em;
	}
</style>
