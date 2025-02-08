<script setup>
defineProps({
	workspaces: Array,
});
</script>

<template>
	<div>
		<h1>Greetings: {{ workspaces }}</h1>
	</div>
</template>
