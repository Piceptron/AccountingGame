// Copyright 1998-2019 Epic Games, Inc. All Rights Reserved.

#include "UnrealGameMode.h"
#include "UnrealCharacter.h"
#include "UObject/ConstructorHelpers.h"

AUnrealGameMode::AUnrealGameMode()
{
	// set default pawn class to our Blueprinted character
	static ConstructorHelpers::FClassFinder<APawn> PlayerPawnBPClass(TEXT("/Game/ThirdPersonCPP/Blueprints/ThirdPersonCharacter"));
	if (PlayerPawnBPClass.Class != NULL)
	{
		DefaultPawnClass = PlayerPawnBPClass.Class;
	}
}
