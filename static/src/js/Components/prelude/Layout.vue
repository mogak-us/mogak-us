<script>
defineProps({
	title: String,
});
</script>

<template>
	<div>
		<header>
			<h1>{{ title }}</h1>
			<!-- Add navigation or other header content here -->
		</header>
		<main>
			<slot></slot>
		</main>
		<footer>
			<!-- Add footer content here -->
		</footer>
	</div>
</template>

<style scoped>
header {
	background-color: #f8f9fa;
	padding: 1rem;
	text-align: center;
}

main {
	padding: 1rem;
}

footer {
	background-color: #f8f9fa;
	padding: 1rem;
	text-align: center;
}
</style>
