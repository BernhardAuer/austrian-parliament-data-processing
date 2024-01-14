<svelte:head>
	<title>Impressum | parli-info.org</title>
</svelte:head>
<script>
    import { env } from '$env/dynamic/public'
    const name = env.PUBLIC_IMPRINT_NAME || '';
    const contact = env.PUBLIC_IMPRINT_CONTACT || '';
    const address = env.PUBLIC_IMPRINT_ADDRESS || '';
</script>

<div class="md:2xl:mx-96">
    <h1 class="text-4xl font-normal leading-normal mt-0 mb-2 text-blue-800 break-words">Impressum</h1>
    <p class="font-bold">Angaben gemäß § 25 Mediengesetz (Österreich) </p> <br>

    Medieninhaber: {name} <br>
    Kontakt: {contact} <br>
    Adresse: {address} <br>

    Diese Seite dient der einfachen Aufbereitung von Parlamentsdaten.
</div>