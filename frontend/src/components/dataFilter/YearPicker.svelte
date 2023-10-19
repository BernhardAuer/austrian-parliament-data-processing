<script>
	import { createEventDispatcher } from 'svelte';
	import DataFilterSelect from './DataFilterSelect.svelte';

	export let selectedYear = null;

	const dispatch = createEventDispatcher();

	const triggerSubmit = () => {
		dispatch('submit', selectedYear);
	};

	// generate array of years, beginning with 1996 till current year
	const yearsSince1996 = new Date().getFullYear() - 1995;
	const yearsWithDigitalizedGPs = Array.from({ length: yearsSince1996 }, (x, i) => i + 1996);
</script>

<h2 class="card-title">Datenfilter</h2>

<DataFilterSelect
	labelText="Jahr"
	tooltipText="Nur jene Jahre, von denen es vollständig digitalisierte Gesetzgebungsperioden gibt, sind auswählbar."
	values={yearsWithDigitalizedGPs}
	bind:selectedValue={selectedYear}
/>

<button class="btn" on:click={triggerSubmit}>Grafik aktualisieren</button>
