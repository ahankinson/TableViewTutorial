/*
 * AppController.j
 * ProjectManager
 *
 * Created by Andrew Hankinson on December 13, 2012.
 * Copyright 2012, Distributed Digital Music Archives and Libraries Lab All rights reserved.
 */

@import <Foundation/CPObject.j>
@import <Ratatosk/Ratatosk.j>


@implementation AppController : CPObject
{
    CPWindow    theWindow; //this "outlet" is connected automatically by the Cib
    @outlet     CPObject    projectController;
}

- (void)applicationDidFinishLaunching:(CPNotification)aNotification
{
    // This is called when the application is done loading.
    [projectController fetchProjects];
}

- (void)awakeFromCib
{
    [WLRemoteLink setDefaultBaseURL:@""];
    // This is called when the cib is done loading.
    // You can implement this method on any object instantiated from a Cib.
    // It's a useful hook for setting up current UI values, and other things.

    // In this case, we want the window from Cib to become our full browser window
    [theWindow setFullPlatformWindow:YES];
}

@end


@implementation Project : WLRemoteObject
{
    CPString    pk                @accessors;
    CPString    projectName       @accessors;
    CPString    shortDescription  @accessors;
    CPDate      startDate         @accessors;
    CPDate      endDate         @accessors;
}

- (id)init
{
    if (self = [super init])
    {
        [self setProjectName:@"New Project"];
        [self setShortDescription:@"Add a short description"];
    }
    return self;
}

+ (CPArray)remoteProperties
{
    return [
        ['pk', 'url'],
        ['projectName', 'project_name'],
        ['shortDescription', 'short_description'],
        ['startDate', 'start_date'],
        ['endDate', 'end_date']
    ];
}

- (CPString)remotePath
{
    if ([self pk])
    {
        return [self pk];
    }
    else
    {
        return @"/projects/";
    }
}
@end


@implementation ProjectController : CPObject
{
    @outlet     CPArrayController   projectArrayController;
}

- (void)fetchProjects
{
    [WLRemoteAction schedule:WLRemoteActionGetType path:'/projects/' delegate:self message:"Loading Projects"];
}

- (void)remoteActionDidFinish:(WLRemoteAction)anAction
{
    projects = [Project objectsFromJson:[anAction result]];
    [projectArrayController addObjects:projects];
}

- (IBAction)newProject:(id)aSender
{
    project = [[Project alloc] init];
    [projectArrayController addObject:project];
    [project ensureCreated];
}

- (IBAction)deleteProject:(id)aSender
{
    selectedObjects = [projectArrayController selectedObjects];
    [projectArrayController removeObjects:selectedObjects];
    [selectedObjects makeObjectsPerformSelector:@selector(ensureDeleted)];
}

@end
