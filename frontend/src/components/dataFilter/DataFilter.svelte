<script>
	import LoadingSpinner from './../LoadingSpinner.svelte';
	import { createEventDispatcher } from 'svelte';
	import DataFilterSelect from './DataFilterSelect.svelte';
	import DataFilterSearch from './DataFilterSearch.svelte';
	import DataFilterPoliticalParties from './DataFilterPoliticalParties.svelte';

	export let selectedFilterOptions = null;

	export let legislatureAndMeetings = null;

	const dispatch = createEventDispatcher();

	const triggerSubmit = () => {
		dispatch('submit', selectedFilterOptions);
	};

	// subscribing ONLY to properties is not possible, so we use this workaround
	$: selectedLegislature = selectedFilterOptions.legislature;
	$: selectedLegislature, resetMeetingFilter();

	let isInitialLoad = true;
	const resetMeetingFilter = () => {	
		if (isInitialLoad == true) {
			isInitialLoad = false;
			return;
		}
		if (selectedFilterOptions.legislature == undefined) {
			return;
		}
		if (Array.isArray(legislatureAndMeetings) && legislatureAndMeetings.length) {
			selectedFilterOptions.meetingNumber = legislatureAndMeetings
				.filter((x) => x.legislature == selectedFilterOptions.legislature)[0]
				.meetings.slice(-1)[0];
		}
	};

</script>

<h2 class="card-title">Datenfilter</h2>
{#if legislatureAndMeetings == null}
	<LoadingSpinner />
{:else}
	<DataFilterSelect
		labelText="Gesetzgebungsperiode"
		tooltipText="Nur vollständig digitalisierte Gesetzgebungsperioden sind verfügbar."
		values={legislatureAndMeetings.map((x) => x.legislature)}
		bind:selectedValue={selectedFilterOptions.legislature}
	/>

	<DataFilterSelect
		labelText="Sitzung"
		tooltipText="Nur Sitzungen mit mind. einer kategorisierten Wortmeldungsart sind verfügbar."
		values={legislatureAndMeetings.find((x) => x.legislature === selectedFilterOptions.legislature)?.meetings}
		bind:selectedValue={selectedFilterOptions.meetingNumber}
	/>

	<DataFilterSearch {selectedFilterOptions} />

	<DataFilterPoliticalParties
		labelText="Fraktion"
		tooltipText="Vorläufig sind nur derzeit im Parlament aktive Fraktionen verfügbar."
		bind:selectedPoliticalParties={selectedFilterOptions.politicalParties}	
	/>

	<button class="btn" on:click={triggerSubmit}>Grafik aktualisieren</button>
{/if}
